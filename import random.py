
"""Création de 4 nombre aléatoire allant dans une liste"""

import time
import random


p = 4
power = []
luminance = []
i = 6
temp_values =[]
wavelength = [1.02, 2.03, 1.3, 1.4]

for j in range(p): #Photodiode
        w = wavelength[j] #Value of the current wavelength
        time.sleep(0.25)

        nombre_aleatoire = random.uniform(9.74674103e-10, 6.97651927e-08)
        temp_values.append(nombre_aleatoire)

        power[j] = temp_values[j]
        print(power[j])

print(power)