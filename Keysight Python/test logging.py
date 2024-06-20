#tests du logging mode
import pyvisa as visa
import json

c = 0
def Errorcheck(N7745C):
    myError = []
    ErrorList = N7745C.query("SYST:ERR?").split(',')#Checking for error messages
    Error = ErrorList[0]

    if int(Error) == 0:
        print ("+0, No Error!")
        
    else:
        while int(Error)!=0:
            print ("Error #: " + ErrorList[0])
            print ("Error Description: " + ErrorList[1])
            
            myError.append(ErrorList[0])
            myError.append(ErrorList[1])
    
            ErrorList = N7745C.query("SYST:ERR?").split(',')
            Error = ErrorList[0]
            myError = list(myError)
            
    return myError


def connection():
        """Connect to the instrument"""
        rm = visa.ResourceManager()
        N7745C = rm.open_resource('TCPIP0::100.65.4.185::inst0::INSTR')
        N7745C.timeout = 10000
        N7745C.write("*CLS")#Clear the event status registers and empty the error queue
        N7745C.write("*IDN?")#Query identification string *IDN?
        #print(N7745C.read())
        if Errorcheck(N7745C) == []: #8 channels on the N7745C
            
            #Preset the N7745C and wait for operation complete via the *OPC?, i.e.
            #the operation complete query.
            N7745C.write("SYST:PRES;*OPC?")
            print("Preset complete, *OPC? returned : " + N7745C.read())
                
            N7745C.write(':configure:measurement:setting:preset')#Reset the settings
            
            N7745C.write(':sense:power:unit:all Watt')#Sets the sensor power unit of all channels to Watt
            print('\n------------------------\n')
        return N7745C
            
def initiate(N7745C,wavelengths):
        """Setting the wavelength for every photodiode"""
        wvUnit = 'um'            
        for w in wavelengths:
            i = wavelengths.index(w)#Index of the loop (starting from 0)
            
            if w <= 1.250:#N7745C only accept as a parameter wavelengths between 1250 and 1650nm
                #Sets the sensor wavelength and its unit.
                N7745C.write(f'sense{i+1}:power:wavelength {1.250}{wvUnit}')
                print(f"set wavelength n°{i} to {w}{wvUnit}")
                
            elif w >= 1.650:
                #Sets the sensor wavelength and its unit.
                N7745C.write(f'sense{i+1}:power:wavelength {1.650}{wvUnit}')
                print(f"set wavelength n°{i} to {w}{wvUnit}")
                
            else:       
                #Sets the sensor wavelength and its unit.
                N7745C.write(f'sense{i+1}:power:wavelength {w}{wvUnit}')
                print(f"set wavelength n°{i} to {w}{wvUnit}")
      
def Errcheck(N7745C):
    print(N7745C.query("SYST:ERR?"))
    
def main():
    wavelengths=[1.07,1.2,1.55,1.65]
    N7745C=connection()
    N7745C.write("SENS1:FUNC:STAT LOGG,STOP") #disables any previous logging
    N7745C.write("SENS1:POW:RANG:AUTO 0")#fixed range needed for logging
    N7745C.write("SENS1:power:unit 1")
    N7745C.write("SENS1:FUNC:PAR:LOGG 10,100ms")
    Errcheck(N7745C)
    initiate(N7745C,wavelengths)
    N7745C.write("trig1:INP MME") #MME for repeating
    Errcheck(N7745C)
    
    #Read the power value of the channel
    N7745C.write("SENS1:FUNC:LOOP 1")
    Errcheck(N7745C)
    #N7745C.write("SENS1:FUNC:LOOP 0")
    N7745C.write("init1:cont 1")
    Errcheck(N7745C)
    
    val = []
    for w in wavelengths:
        values = N7745C.query_binary_values(':SENSe1:FUNCtion:RESult:BUFA?', datatype="f",is_big_endian = False)
        Errcheck(N7745C)
        for i in values:
            print(i,end=",")
            val.append(i)
        print()
    N7745C.write("SENS1:FUNC:STAT LOGG,STOP") #disables any previous logging
    return val
val = main()

with open("logging values.json", 'w+') as file:
    json.dump(val,file,ensure_ascii=False)