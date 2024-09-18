
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