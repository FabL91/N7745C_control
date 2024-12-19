"""test de logging sur le l'instrument keysight N7745 C"""

#from keysight_ktn7740 import *
import pyvisa as visa
# NOTE: the default pyvisa import works well for Python 3.6+ # if you are working with python version lower than 3.6, use 'import visa' instead of import pyvisa as visa
import time # start of Untitled


rm=visa.ResourceManager()
list_visa = rm.list_resources
print(list_visa)
N7745C=rm.open_resource('TCPIP0::169.254.241.203::inst0::INSTR')

print(N7745C.query("*IDN?")) #The IDeNtification query 

#N7745C.write(":SYSTem:PRESet") #Sets the insrument to its standard settings
N7745C.write(":SENSe2:FUNCtion:STATe LOGG,STOP") #Enables/Disables the logging, MinMax, or stability data acquisition function mode
N7745C.write(":SENSe2:POWer:GAIN:AUTO 0") #Set the Auto Gain
N7745C.write(":SENSe2:POWer:RANGe:AUTO 0") #Enables or disables automatic power ranging for the slot
N7745C.write(":SENSe2:POWer:RANGe:UPPer -10 DBM") #Sets the power range for the module.
N7745C.write(":SENSe2:POWer:UNIT 1") #Sets the sensor power unit 
N7745C.write(":SENSe2:POWer:WAVelength 1552NM")#Sets the sensor wavelength.
N7745C.write(":SENSe2:FUNCtion:PARameter:LOGGing 10,100 MS")#Sets the number of data points and the averaging time for the logging data acquisition function
N7745C.write(":TRIGger2:INPut IGN")#Sets the incoming trigger response and arms the slot


N7745C.write(":SENSe2:FUNCtion:LOOP 0")

N7745C.write(":SENSe2:FUNCtion:STATe LOGG,STAR")#Enables/Disables the logging

# Loop until status is 'LOGGING_STABILITY,COMPLETE'

datalist = []
n=10
data_1 = 0
t = 1
opc = 0
#start_time = time.perf_counter()

"""while data_1 == 0:
    # Modifier data pour éventuellement sortir de la boucle
    time.sleep(0.5)
    data_1 = N7745C.query(":SENS2:FUNC:RES:IND?")
    datalist.append(data_1)

    print(data_1)
    print(datalist)"""    


start_time = time.perf_counter()
   
while opc == 0:
    opc = N7745C.query("*OPC?")
    
time.sleep(t)

print(opc)


end_time = time.perf_counter()
duration = end_time - start_time  # Calcule la durée d'exécution
 

data = N7745C.query_binary_values(':SENSE2:CHANnel:FUNCtion:RESult?','f',False)

print(data)
print(len(data))
print(f"\nDurée d'exécution : {duration:.2f} secondes")


      

N7745C.write(":SENSe2:FUNCtion:STATe LOGG,STOP")

N7745C.close()
rm.close()










