#importing files
import logging
import plck
import time
#This program connects to a N7745C and takes a power reading at the specified wavelength.
#One wavelength per channel

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s', filename='Logging_Mesure.log', level=logging.INFO)

def Init_Mesure(N7745C, nbre_pts, Aver_Time, unit):

    print("début Initialisation des mesures")

    #N7745C.write(":SYSTem:PRESet") #Sets the insrument to its standard settings
    N7745C.write(":SENSe1:FUNCtion:STATe LOGG,STOP")
    N7745C.write(":SENSe2:FUNCtion:STATe LOGG,STOP")
    N7745C.write(":SENSe3:FUNCtion:STATe LOGG,STOP")
    N7745C.write(":SENSe4:FUNCtion:STATe LOGG,STOP")

    N7745C.write(":SENSe1:POWer:GAIN:AUTO 0")
    N7745C.write(":SENSe2:POWer:GAIN:AUTO 0")
    N7745C.write(":SENSe3:POWer:GAIN:AUTO 0")
    N7745C.write(":SENSe4:POWer:GAIN:AUTO 0")

    N7745C.write(":SENSe1:POWer:RANGe:UPPer -10 DBM")
    N7745C.write(":SENSe2:POWer:RANGe:UPPer -10 DBM")
    N7745C.write(":SENSe3:POWer:RANGe:UPPer -10 DBM")
    N7745C.write(":SENSe4:POWer:RANGe:UPPer -10 DBM")
    
    N7745C.write(":SENSe1:POWer:UNIT 1")
    N7745C.write(":SENSe2:POWer:UNIT 1")
    N7745C.write(":SENSe3:POWer:UNIT 1")
    N7745C.write(":SENSe4:POWer:UNIT 1")

    #N7745C.write(f":SENSe1:FUNCtion:PARameter:LOGGing {nbre_pts},{Aver_Time} {unit}")
    N7745C.write(f":SENSe1:FUNCtion:PARameter:LOGGing {nbre_pts},{Aver_Time} {unit}")#Sets the number of data points and the averaging time for the logging data acquisition function
    N7745C.write(f":SENSe2:FUNCtion:PARameter:LOGGing {nbre_pts},{Aver_Time} {unit}")#
    N7745C.write(f":SENSe3:FUNCtion:PARameter:LOGGing {nbre_pts},{Aver_Time} {unit}")#
    N7745C.write(f":SENSe4:FUNCtion:PARameter:LOGGing {nbre_pts},{Aver_Time} {unit}")#

    N7745C.write(":TRIGger1:INPut IGN")
    N7745C.write(":TRIGger2:INPut IGN")
    N7745C.write(":TRIGger3:INPut IGN")
    N7745C.write(":TRIGger4:INPut IGN")


    N7745C.write(":SENSe1:FUNCtion:LOOP 0")
    N7745C.write(":SENSe2:FUNCtion:LOOP 0")
    N7745C.write(":SENSe3:FUNCtion:LOOP 0")
    N7745C.write(":SENSe4:FUNCtion:LOOP 0")
    #N7745C.write(":SENSe1:FUNCtion:STATe LOGG,STAR")

    print("fin Initialisation des mesures")

def run(N7745C, Delay_R_Buf, state, temperatureListK, temperature, returnedpower, returnedlum, wavelength):
    p = len(wavelength)
    power = returnedpower
    luminance = returnedlum
    i = temperatureListK.index(temperature)
    Delay_R_Buf = float(Delay_R_Buf)
     # Activation de la mesure
    N7745C.write(f":SENSe1:FUNCtion:STATe LOGG,STAR")
    logger.info(f"Starting logging for channel 1")  # Initialisation des variables pour chaque canal
    N7745C.write(f":SENSe2:FUNCtion:STATe LOGG,STAR")
    logger.info(f"Starting logging for channel 2")  # Initialisation des variables pour chaque canal
    N7745C.write(f":SENSe3:FUNCtion:STATe LOGG,STAR")
    logger.info(f"Starting logging for channel 3")  # Initialisation des variables pour chaque canal
    N7745C.write(f":SENSe4:FUNCtion:STATe LOGG,STAR")
    logger.info(f"Starting logging for channel 4")  # Initialisation des variables pour chaque canal

    """Looging_canals(N7745C,1)
    Looging_canals(N7745C,2)
    Looging_canals(N7745C,3)
    Looging_canals(N7745C,4)"""

    all_temp_values = []  # Liste pour stocker toutes les valeurs de temp_values
    
    for j in range(p):  # Photodiode
        w = wavelength[j]  # Valeur de la longueur d'onde actuelle
        
        data_1 = 0      
   
        while data_1 == 0 :
                
                data_1 = N7745C.query("*OPC?")
       
        time.sleep(Delay_R_Buf)

        logger.info(f"début lecture Buffer canal:{j + 1}")
        temp_values = N7745C.query_binary_values(f":SENSE{j + 1}:CHANnel:FUNCtion:RESult?",'f',False)
        logger.info(f"fin lecture Buffer canal:{j + 1}")
                
        

        #print(temp_values)

        if state == 'calib':     #rajouter condition sur calib ou sample
            power[j][i] = temp_values[0]
            luminance[j][i] = plck.planck(w, temperature)
            
        elif state =='sample':
            power[j] = temp_values[0]
            
        N7745C.write(f":SENSe{j + 1}:FUNCtion:STATe LOGG,STOP")
        all_temp_values.append(temp_values)
        

       
    if state == 'calib':
        return power, luminance
    
    else: #we do not return luminance for the sample measurement
        return power, all_temp_values
   
'''    
Luminance and Power matrices are defined like this :
    [ [X11, X12, ..., X1j, ..., X1p],   1
      [X21, X22, ..., X2j, ..., X2p],   |
                 ...                ,   |
      [Xi1, Xi2, ..., Xij, ..., Xip],   j
                 ...                    |
      [Xn1, Xn2, ..., Xnj, ..., Xnp] ]  V
                                        p (Index of Photodiode <=> Index of Wavelength)
                                        
     1 ------------ i --------------> n (Temperature)
'''

def calibration(N7745C, Delay_R_Buf, temperatureListK, temperature, returnedpower, returnedlum,
                wavelength):
                    
    #Getting the values of wavelength, power and luminance
    returnedpower, returnedlum = run(N7745C, Delay_R_Buf, 'calib', temperatureListK, temperature, returnedpower, returnedlum, wavelength)
    return returnedpower, returnedlum

"""def Looging_canals(N7745C,Numero_canal):


    data_1 = 0      
   
    while data_1 == 0 :
            print(f"La valeur de data est toujours {data_1}")
            data_1 = N7745C.query(f":SENS{Numero_canal}:FUNC:RES:IND?") """      

                
    
    

