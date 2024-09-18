#importing files
import plck
import time
import random

#This program connects to a N7745C and takes a power reading at the specified wavelength.
#One wavelength per channel


def run(N7745C, state, simu, temperatureListK, temperature, returnedpower, returnedlum, wavelength):    
    p = len(wavelength)
    power = returnedpower
    luminance = returnedlum
    i = temperatureListK.index(temperature)
    #temp_values = []
            
    
    for j in range(p): #Photodiode
        w = wavelength[j] #Value of the current wavelength
        #time.sleep(0.25)
        #Read the power value of the channel
        
        if not simu:
            temp_values = N7745C.query_ascii_values('read{}:power?'.format(j + 1))
            print(f"{temp_values} - query read power")
        else:
            if state == 'calib':
                if i == 0:
                    temp_values = [7.74674103e-10, 5.26310051e-10, 5.25565991e-09, 6.50368026e-09]
                elif i == 1:
                    temp_values = [2.45340437e-09, 2.2590938e-09, 1.636859e-08, 1.88642915e-08]
                elif i == 2:
                    temp_values = [6.58381305e-09, 7.19122983e-09, 4.02801845e-08, 4.39034693e-08]
                elif i == 3:
                    temp_values = [1.58998219e-08, 1.91025418e-08, 8.60866933e-08, 8.95260399e-08]
                elif i == 4:
                    temp_values = [3.42846675e-08, 4.3034472e-08, 1.61733809e-07, 1.61775887e-07]
                elif i == 5:
                    temp_values = [6.97651927e-08, 8.90161687e-08, 2.84452966e-07, 2.7463679e-07]
                    
        if state == 'calib':     #rajouter condition sur calib ou sample
            power[j][i] = temp_values[0]
            luminance[j][i] = plck.planck(w, temperature)
            
        elif state =='sample':

            if simu:
                nombre_aleatoire = random.uniform(9.74674103e-10, 6.97651927e-08)
                temp_values.append(nombre_aleatoire)
                power[j] = temp_values[j]
                print(f"{power[j]} - power[j]")

            else:
                #power[j] = temp_values[0] valeur modifié à vérifier avec le N7745C
                power[j] = temp_values[0]
                print(f"{power[j]} - power[j]")
            
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

#def calibration(N7745C, temperatureListK, temperature, returnedpower, returnedlum, wavelength):
def calibration(N7745C, simu, temperatureListK, temperature, returnedpower, returnedlum, wavelength):                    
    
    #Getting the values of wavelength, power and luminance
    returnedpower, returnedlum = run(N7745C, 'calib', simu, temperatureListK, temperature, returnedpower, returnedlum, wavelength)
    return returnedpower, returnedlum