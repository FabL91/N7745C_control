
import time
import numpy as np
"""config du powermeter pour une acquisition rapide"""

def run(N7745C, nbre_pts, Aver_Time, unit, Delay_R_Buf):



    Delay_R_Buf = float(Delay_R_Buf)

    N7745C.write(":SYSTem:PRESet") #Sets the insrument to its standard settings

    N7745C.write(f":SENSe1:FUNCtion:STATe LOGG,STOP") #Enables/Disables the logging, MinMax, or stability data acquisition function mode
    N7745C.write(f":SENSe2:FUNCtion:STATe LOGG,STOP")
    N7745C.write(f":SENSe3:FUNCtion:STATe LOGG,STOP")
    N7745C.write(f":SENSe4:FUNCtion:STATe LOGG,STOP")

    N7745C.write(f":SENSe1:POWer:GAIN:AUTO 0")
    N7745C.write(f":SENSe2:POWer:GAIN:AUTO 0") #Set the Auto Gain
    N7745C.write(f":SENSe3:POWer:GAIN:AUTO 0")
    N7745C.write(f":SENSe4:POWer:GAIN:AUTO 0")

    N7745C.write(f":SENSe1:POWer:RANGe:AUTO 0") #Enables or disables automatic power ranging for the slot
    N7745C.write(f":SENSe2:POWer:RANGe:AUTO 0")
    N7745C.write(f":SENSe3:POWer:RANGe:AUTO 0")
    N7745C.write(f":SENSe4:POWer:RANGe:AUTO 0")
    
    N7745C.write(f":SENSe1:POWer:RANGe:UPPer -10 DBM") #Sets the power range for the module.
    N7745C.write(f":SENSe2:POWer:RANGe:UPPer -10 DBM")
    N7745C.write(f":SENSe3:POWer:RANGe:UPPer -10 DBM")
    N7745C.write(f":SENSe4:POWer:RANGe:UPPer -10 DBM")

    N7745C.write(f":SENSe1:POWer:UNIT 1")
    N7745C.write(f":SENSe2:POWer:UNIT 1")
    N7745C.write(f":SENSe3:POWer:UNIT 1")
    N7745C.write(f":SENSe4:POWer:UNIT 1")


    N7745C.write(f":SENSe1:FUNCtion:PARameter:LOGGing {nbre_pts},{Aver_Time} {unit}")#Sets the number of data points and the averaging time for the logging data acquisition function
    N7745C.write(f":SENSe2:FUNCtion:PARameter:LOGGing {nbre_pts},{Aver_Time} {unit}")
    N7745C.write(f":SENSe3:FUNCtion:PARameter:LOGGing {nbre_pts},{Aver_Time} {unit}")
    N7745C.write(f":SENSe4:FUNCtion:PARameter:LOGGing {nbre_pts},{Aver_Time} {unit}")
    
    N7745C.write(f":TRIGger1:INPut IGN")#Sets the incoming trigger response and arms the slot
    N7745C.write(f":TRIGger2:INPut IGN")
    N7745C.write(f":TRIGger3:INPut IGN")
    N7745C.write(f":TRIGger4:INPut IGN")

    N7745C.write(f":SENSe1:FUNCtion:STATe LOGG,STAR")#Enables/Disables the logging
    N7745C.write(f":SENSe2:FUNCtion:STATe LOGG,STAR")
    N7745C.write(f":SENSe3:FUNCtion:STATe LOGG,STAR")
    N7745C.write(f":SENSe4:FUNCtion:STATe LOGG,STAR")
    
    status = N7745C.query(f":SENSe1:FUNCtion:STATe?")
    counter = 0 # Initialize counter for iterations
    start_time = time.time() # Initialize timer

    status_phd_2 = N7745C.query(f":SENSe2:FUNCtion:STATe?")
    counter_phd_2 = 0 # Initialize counter for iterations
    start_time_phd_2 = time.time() # Initialize timer  
    
    status_phd_3 = N7745C.query(f":SENSe3:FUNCtion:STATe?")
    counter_phd_3 = 0 # Initialize counter for iterations
    start_time_phd_3 = time.time() # Initialize timer

    status_phd_4 = N7745C.query(f":SENSe4:FUNCtion:STATe?")
    counter_phd_4 = 0 # Initialize counter for iterations
    start_time_phd_4 = time.time() # Initialize timer

    while "COMPLETE" not in status and "COMPLETE" not in status_phd_2 and "COMPLETE" not in status_phd_3 and "COMPLETE" not in status_phd_4:
                
        status = N7745C.query(f":SENSe1:FUNCtion:STATe?")
        # Increment counter9
        counter += 1  

        status_phd_2 = N7745C.query(f":SENSe2:FUNCtion:STATe?")
        # Increment counter9
        counter_phd_2 += 1  

        status_phd_3 = N7745C.query(f":SENSe3:FUNCtion:STATe?")
        # Increment counter9
        counter_phd_3 += 1

        status_phd_4 = N7745C.query(f":SENSe4:FUNCtion:STATe?")
        # Increment counter9
        counter_phd_4 += 1
        
        time.sleep(Delay_R_Buf)    # Wait for a specified time before querying again (e.g., 1 second)
                        
        
        # Optionally, print the status to monitor the progress
        elapsed_time = time.time() - start_time
        print(f"Iteration {counter}: Current status: {status}, Time elapsed: {elapsed_time:.2f} seconds")

        elapsed_time_phd_2 = time.time() - start_time_phd_2
        print(f"Iteration Phd 2 {counter_phd_2}: Current status Phd 2: {status_phd_2}, Time elapsed Phd 2: {elapsed_time_phd_2:.2f} seconds")

        elapsed_time_phd_3 = time.time() - start_time_phd_3
        print(f"Iteration Phd 3 {counter_phd_3}: Current status Phd 3: {status_phd_3}, Time elapsed Phd 3: {elapsed_time_phd_3:.2f} seconds")

        elapsed_time_phd_4 = time.time() - start_time_phd_4
        print(f"Iteration Phd 4 {counter_phd_4}: Current status Phd 4: {status_phd_4}, Time elapsed Phd 4: {elapsed_time_phd_4:.2f} seconds")

    elapsed_time = time.time() - start_time
    print(f"Status is COMPLETE. Exiting loop after {counter} iterations and {elapsed_time:.2f} seconds.")

    elapsed_time_phd_2 = time.time() - start_time_phd_2
    print(f"Status Phd 2 is COMPLETE. Exiting loop after {counter_phd_2} iterations and {elapsed_time_phd_2:.2f} seconds.")

    elapsed_time_phd_3 = time.time() - start_time_phd_3
    print(f"Status Phd 3 is COMPLETE. Exiting loop after {counter_phd_3} iterations and {elapsed_time_phd_3:.2f} seconds.")

    elapsed_time_phd_4 = time.time() - start_time_phd_4
    print(f"Status Phd 4 is COMPLETE. Exiting loop after {counter_phd_4} iterations and {elapsed_time_phd_4:.2f} seconds.")

    time.sleep(Delay_R_Buf)

    data = N7745C.query_binary_values(f":SENSE1:CHANnel:FUNCtion:RESult?",'f',False)
    temps = list(0 + np.arange(int(nbre_pts)) * int(Aver_Time))  # On ajoute 1 à valeur_finale pour inclure la valeur finale

    time.sleep(Delay_R_Buf)

    data_phd_2 = N7745C.query_binary_values(f":SENSE2:CHANnel:FUNCtion:RESult?",'f',False)
    #temps_phd_2 = list(0 + np.arange(int(nbre_pts)) * int(Aver_Time))  # On ajoute 1 à valeur_finale pour inclure la valeur finale

    time.sleep(Delay_R_Buf)

    data_phd_3 = N7745C.query_binary_values(f":SENSE3:CHANnel:FUNCtion:RESult?",'f',False)
    #temps_phd_3 = list(0 + np.arange(int(nbre_pts)) * int(Aver_Time))

    time.sleep(Delay_R_Buf)

    data_phd_4 = N7745C.query_binary_values(f":SENSE4:CHANnel:FUNCtion:RESult?",'f',False)
    #temps_phd_4 = list(0 + np.arange(int(nbre_pts)) * int(Aver_Time))

    print(Delay_R_Buf)
    
    return data, temps, data_phd_2, data_phd_3, data_phd_4
    




def you():
    """test des variables globales entre les fonctions"""

    values = []  # Liste globale pour stocker les valeurs
    for i in range(10):  # Par exemple, on incrémente 10 fois
        values.append(i)
        # ... (autres traitements)
        time.sleep(0.1)
        print(i)

