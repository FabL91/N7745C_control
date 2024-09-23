
import time

for i in range(10):
    start_time = time.time_ns()  # Mesure le temps en nanosecondes
    # Ici, tu places le code que tu veux exécuter à chaque itération
    # Par exemple, un simple affichage :
    print(f"Itération {i+1}")
    print("gone")

    end_time = time.time_ns()
    elapsed_time_ns = end_time - start_time
    elapsed_time_us = elapsed_time_ns // 1000  # Conversion en microsecondes
    print(f"Temps écoulé pour l'itération {i+1} : {elapsed_time_us} microsecondes")


import numpy as np

def generate_ramp(x0, xe, dx):
    # Créer un tableau de points allant de x0 à xe avec un intervalle dx
    x_values = np.arange(x0, xe + dx, dx)
    return x_values

# Exemple d'utilisation
x0 = 0       # Valeur initiale
xe = 10      # Valeur finale
dx = 0.5     # Intervalle entre deux points

ramp_points = generate_ramp(x0, xe, dx)
print(ramp_points)

import numpy as np

def generate_ramp_1(x0, xe, dx):
    # Générer le nombre de points en partant de x0 avec un intervalle dx
    x_values = x0 + np.arange(xe) * dx
    return x_values

# Exemple d'utilisation
x0 = 0       # Valeur initiale
xe = 10      # Nombre de points à générer
dx = 100     # Intervalle entre deux points

ramp_points = list(generate_ramp_1(x0, xe, dx))
print(ramp_points)

xar = list(np.linspace(0, 10, 9))
print(xar)