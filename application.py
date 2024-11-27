#importing files
import plck
import time
#This program connects to a N7745C and takes a power reading at the specified wavelength.
#One wavelength per channel

def Init_Mesure(N7745C):

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
    N7745C.write(":SENSe1:FUNCtion:PARameter:LOGGing 2,1 MS")#Sets the number of data points and the averaging time for the logging data acquisition function
    N7745C.write(":SENSe2:FUNCtion:PARameter:LOGGing 2,1 MS")#
    N7745C.write(":SENSe3:FUNCtion:PARameter:LOGGing 2,1 MS")#
    N7745C.write(":SENSe4:FUNCtion:PARameter:LOGGing 2,1 MS")#

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

def run(N7745C, state, temperatureListK, temperature, returnedpower, returnedlum, wavelength):
    p = len(wavelength)
    power = returnedpower
    luminance = returnedlum
    i = temperatureListK.index(temperature)

    N7745C.write(":SENSe1:FUNCtion:STATe LOGG,STAR")
    N7745C.write(":SENSe2:FUNCtion:STATe LOGG,STAR")
    N7745C.write(":SENSe3:FUNCtion:STATe LOGG,STAR")
    N7745C.write(":SENSe4:FUNCtion:STATe LOGG,STAR")

    status_1 = N7745C.query(":SENSe1:FUNCtion:STATe?")
    counter_1 = 0 # Initialize counter for iterations
    start_time_1 = time.time() # Initialize timer

    status_2 = N7745C.query(":SENSe2:FUNCtion:STATe?")
    counter_2 = 0 # Initialize counter for iterations
    start_time_2 = time.time() # Initialize timer

    status_3 = N7745C.query(":SENSe3:FUNCtion:STATe?")
    counter_3 = 0 # Initialize counter for iterations
    start_time_3 = time.time() # Initialize timer

    status_4 = N7745C.query(":SENSe4:FUNCtion:STATe?")
    counter_4 = 0 # Initialize counter for iterations
    start_time_4 = time.time() # Initialize timer
    

    for j in range(p): #Photodiode
        w = wavelength[j] #Value of the current wavelength
        time.sleep(0.5)
        #Read the power value of the channel
        #temp_values = N7745C.query_ascii_values('read{}:power?'.format(j + 1))
        
        
        
        
        while "COMPLETE" not in status_1 and "COMPLETE" not in status_2 and "COMPLETE" not in status_3 and "COMPLETE" not in status_4:

            status_1 = N7745C.query(":SENSe1:FUNCtion:STATe?")
            # Increment counter9
            counter_1 += 1
            time.sleep(1)

            elapsed_time_1 = time.time() - start_time_1
            print(f"Iteration {counter_1}: Current status: {status_1}, Time elapsed: {elapsed_time_1:.2f} seconds")

            status_2 = N7745C.query(":SENSe2:FUNCtion:STATe?")
            # Increment counter9
            counter_2 += 1
            time.sleep(1)

            elapsed_time_2 = time.time() - start_time_2
            print(f"Iteration {counter_2}: Current status: {status_2}, Time elapsed: {elapsed_time_2:.2f} seconds")

            status_3 = N7745C.query(":SENSe3:FUNCtion:STATe?")
            # Increment counter9
            counter_3 += 1
            time.sleep(1)

            elapsed_time_4 = time.time() - start_time_4
            print(f"Iteration {counter_4}: Current status: {status_4}, Time elapsed: {elapsed_time_4:.2f} seconds")

            status_4 = N7745C.query(":SENSe4:FUNCtion:STATe?")
            # Increment counter9
            counter_4 += 1
            time.sleep(1)

            elapsed_time_4 = time.time() - start_time_4
            print(f"Iteration {counter_4}: Current status: {status_4}, Time elapsed: {elapsed_time_4:.2f} seconds")

        elapsed_time_1 = time.time() - start_time_1
        print(f"Status is COMPLETE. Exiting loop after {counter_1} iterations and {elapsed_time_1:.2f} seconds.")

        elapsed_time_2 = time.time() - start_time_2
        print(f"Status is COMPLETE. Exiting loop after {counter_2} iterations and {elapsed_time_2:.2f} seconds.")

        elapsed_time_3 = time.time() - start_time_3
        print(f"Status is COMPLETE. Exiting loop after {counter_3} iterations and {elapsed_time_3:.2f} seconds.")

        elapsed_time_4 = time.time() - start_time_4
        print(f"Status is COMPLETE. Exiting loop after {counter_4} iterations and {elapsed_time_4:.2f} seconds.")


        
        temp_values = N7745C.query_binary_values(":SENSE{}:CHANnel:FUNCtion:RESult?".format(j + 1),'f',False)

        print(temp_values)

        if state == 'calib':     #rajouter condition sur calib ou sample
            power[j][i] = temp_values[0]
            luminance[j][i] = plck.planck(w, temperature)
            
        elif state =='sample':
            power[j] = temp_values[0]

    N7745C.write(":SENSe1:FUNCtion:STATe LOGG,STOP")
    N7745C.write(":SENSe2:FUNCtion:STATe LOGG,STOP")
    N7745C.write(":SENSe3:FUNCtion:STATe LOGG,STOP")
    N7745C.write(":SENSe4:FUNCtion:STATe LOGG,STOP")       
    
    if state == 'calib':
        return power, luminance
    
    else: #we do not return luminance for the sample measurement
        return power
   
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

def calibration(N7745C, temperatureListK, temperature, returnedpower, returnedlum,
                wavelength):
                    
    #Getting the values of wavelength, power and luminance
    returnedpower, returnedlum = run(N7745C, 'calib', temperatureListK, temperature, returnedpower, returnedlum, wavelength)
    return returnedpower, returnedlum


"""def run(N7745C, state, temperatureListK, temperature, returnedpower, returnedlum, wavelength):
    p = len(wavelength)
    power = returnedpower
    luminance = returnedlum
    i = temperatureListK.index(temperature)
    
    for j in range(p): #Photodiode
        w = wavelength[j] #Value of the current wavelength
        
        #Read the power value of the channel
        temp_values = N7745C.query_ascii_values('read{}:power?'.format(j + 1))
        
        if state == 'calib':     #rajouter condition sur calib ou sample
            power[j][i] = temp_values[0]
            luminance[j][i] = plck.planck(w, temperature)
            
        elif state =='sample':
            power[j] = temp_values[0]
            
    
    if state == 'calib':
        return power, luminance
    
    else: #we do not return luminance for the sample measurement
        return power
   
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

def calibration(N7745C, temperatureListK, temperature, returnedpower, returnedlum,
                wavelength):
                    
    #Getting the values of wavelength, power and luminance
    returnedpower, returnedlum = run(N7745C, 'calib', temperatureListK, temperature, returnedpower, returnedlum, wavelength)
    return returnedpower, returnedlum"""