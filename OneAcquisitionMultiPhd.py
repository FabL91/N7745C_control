
import time
import numpy as np
"""config du powermeter pour une acquisition rapide"""

def run(N7745C, NumPhd, nbre_pts, Aver_Time, unit, phd_1):

    N7745C.write(":SYSTem:PRESet") #Sets the insrument to its standard settings

    N7745C.write(f":SENSe{NumPhd}:FUNCtion:STATe LOGG,STOP") #Enables/Disables the logging, MinMax, or stability data acquisition function mode
    N7745C.write(f":SENSe2:FUNCtion:STATe LOGG,STOP")

    N7745C.write(f":SENSe{NumPhd}:POWer:GAIN:AUTO 0")
    N7745C.write(f":SENSe2:POWer:GAIN:AUTO 0") #Set the Auto Gain

    N7745C.write(f":SENSe{NumPhd}:POWer:RANGe:AUTO 0") #Enables or disables automatic power ranging for the slot
    N7745C.write(f":SENSe2:POWer:RANGe:AUTO 0")

    N7745C.write(f":SENSe{NumPhd}:POWer:RANGe:UPPer -10 DBM") #Sets the power range for the module.
    N7745C.write(f":SENSe2:POWer:RANGe:UPPer -10 DBM")

    N7745C.write(f":SENSe{NumPhd}:POWer:UNIT 1")
    N7745C.write(f":SENSe2:POWer:UNIT 1")

    N7745C.write(f":SENSe{NumPhd}:FUNCtion:PARameter:LOGGing {nbre_pts},{Aver_Time} {unit}")#Sets the number of data points and the averaging time for the logging data acquisition function
    N7745C.write(f":SENSe2:FUNCtion:PARameter:LOGGing {nbre_pts},{Aver_Time} {unit}")
    
    N7745C.write(f":TRIGger{NumPhd}:INPut IGN")#Sets the incoming trigger response and arms the slot
    N7745C.write(f":TRIGger2:INPut IGN")

    N7745C.write(f":SENSe{NumPhd}:FUNCtion:STATe LOGG,STAR")#Enables/Disables the logging
    N7745C.write(f":SENSe2:FUNCtion:STATe LOGG,STAR")
    
    status = N7745C.query(f":SENSe{NumPhd}:FUNCtion:STATe?")
    counter = 0 # Initialize counter for iterations
    start_time = time.time() # Initialize timer

    status_phd_2 = N7745C.query(f":SENSe2:FUNCtion:STATe?")
    counter_phd_2 = 0 # Initialize counter for iterations
    start_time_phd_2 = time.time() # Initialize timer  
    

    while "COMPLETE" not in status and "COMPLETE" not in status_phd_2:
                
        status = N7745C.query(f":SENSe{NumPhd}:FUNCtion:STATe?")
        # Increment counter9
        counter += 1  

        status_phd_2 = N7745C.query(f":SENSe2:FUNCtion:STATe?")
        # Increment counter9
        counter_phd_2 += 1   
        
        time.sleep(0.50)    # Wait for a specified time before querying again (e.g., 1 second)
                        
        
        # Optionally, print the status to monitor the progress
        elapsed_time = time.time() - start_time
        print(f"Iteration {counter}: Current status: {status}, Time elapsed: {elapsed_time:.2f} seconds")

        elapsed_time_phd_2 = time.time() - start_time_phd_2
        print(f"Iteration Phd 2 {counter_phd_2}: Current status Phd 2: {status_phd_2}, Time elapsed Phd 2: {elapsed_time_phd_2:.2f} seconds")

    elapsed_time = time.time() - start_time
    print(f"Status is COMPLETE. Exiting loop after {counter} iterations and {elapsed_time:.2f} seconds.")

    elapsed_time_phd_2 = time.time() - start_time_phd_2
    print(f"Status Phd 2 is COMPLETE. Exiting loop after {counter_phd_2} iterations and {elapsed_time_phd_2:.2f} seconds.")

    data = N7745C.query_binary_values(f":SENSE{NumPhd}:CHANnel:FUNCtion:RESult?",'f',False)
    temps = list(0 + np.arange(int(nbre_pts)) * int(Aver_Time))  # On ajoute 1 à valeur_finale pour inclure la valeur finale

    time.sleep(0.50)

    data_phd_2 = N7745C.query_binary_values(f":SENSE2:CHANnel:FUNCtion:RESult?",'f',False)
    temps_phd_2 = list(0 + np.arange(int(nbre_pts)) * int(Aver_Time))  # On ajoute 1 à valeur_finale pour inclure la valeur finale
    
    return data, temps, data_phd_2, temps_phd_2
    




def you():
    """test des variables globales entre les fonctions"""

    values = []  # Liste globale pour stocker les valeurs
    for i in range(10):  # Par exemple, on incrémente 10 fois
        values.append(i)
        # ... (autres traitements)
        time.sleep(0.1)
        print(i)

