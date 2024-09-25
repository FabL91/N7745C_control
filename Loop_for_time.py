
import time
import numpy as np
import random


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


def generate_ramp(x0, xe, dx):
    # Créer un tableau de points allant de x0 à xe avec un intervalle dx
    x_values = np.arange(x0, xe + dx, dx)
    return x_values



def generate_ramp_1(x0, xe, dx):
    # Générer le nombre de points en partant de x0 avec un intervalle dx
    x_values = x0 + np.arange(xe) * dx
    return x_values


def generer_nombres_aleatoires(N, borne_inferieure, borne_superieure):
  """
  Génère une liste de N nombres aléatoires entre deux bornes.

  Args:
    N: Le nombre de nombres aléatoires à générer.
    borne_inferieure: La borne inférieure de l'intervalle.
    borne_superieure: La borne supérieure de l'intervalle.

  Returns:
    Une liste contenant les nombres aléatoires générés.
  """

  liste_aleatoire = []
  for _ in range(N):
    nombre_aleatoire = random.uniform(borne_inferieure, borne_superieure)
    liste_aleatoire.append(nombre_aleatoire)
  return liste_aleatoire

"""# Exemple d'utilisation :
N = 10  # Générer 10 nombres aléatoires
borne_inf = 7.478704320000001e-10
borne_sup = 7.478704320000001e-8
ma_liste = generer_nombres_aleatoires(N, borne_inf, borne_sup)
print(ma_liste)"""