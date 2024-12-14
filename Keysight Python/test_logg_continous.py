from keysight_ktn7740 import *
import pyvisa as visa
import time
import numpy as np

rm = visa.ResourceManager()
N7745C = rm.open_resource('TCPIP0::169.254.241.203::inst0::INSTR')

print(N7745C.query("*IDN?"))

# Configuration initiale pour les 4 canaux
for channel in range(1, 5):
    N7745C.write(f":SENSe{channel}:FUNCtion:STATe LOGG,STOP")
    N7745C.write(f":SENSe{channel}:POWer:GAIN:AUTO 0")
    N7745C.write(f":SENSe{channel}:POWer:RANGe:AUTO 0")
    N7745C.write(f":SENSe{channel}:POWer:RANGe:UPPer -10 DBM")
    N7745C.write(f":SENSe{channel}:POWer:UNIT 1")
    N7745C.write(f":SENSe{channel}:POWer:WAVelength 1552NM")
    N7745C.write(f":SENSe{channel}:FUNCtion:PARameter:LOGGing 100,10 US")
    N7745C.write(f":TRIGger{channel}:INPut IGN")
    N7745C.write(f":SENSe{channel}:FUNCtion:LOOP 0")

try:
    while True:
        # Démarrer l'acquisition sur tous les canaux
        for channel in range(1, 5):
            N7745C.write(f":SENSe{channel}:FUNCtion:STATe LOGG,STAR")

        # Attendre que l'acquisition soit terminée sur tous les canaux
        all_complete = False
        while not all_complete:
            statuses = [int(N7745C.query(f":SENS{channel}:FUNC:RES:IND?")) for channel in range(1, 5)]
            all_complete = all(status == 1 for status in statuses)
            time.sleep(0.01)

        # Ajouter un délai avant la lecture des données
        time.sleep(0.5)

        # Lire les données de tous les canaux
        data = []
        for channel in range(1, 5):
            channel_data = N7745C.query_binary_values(f':SENSE{channel}:CHANnel:FUNCtion:RESult?', 'f', False)
            data.append(channel_data)

        # Traiter les données (exemple : calculer la moyenne pour chaque canal)
        for channel, channel_data in enumerate(data, 1):
            mean_value = np.mean(channel_data)
            print(f"Canal {channel} moyenne: {mean_value}")

        # Optionnel : ajouter un délai entre les acquisitions
        time.sleep(1)

except KeyboardInterrupt:
    print("Acquisition arrêtée par l'utilisateur")

finally:
    # Arrêter l'acquisition sur tous les canaux
    for channel in range(1, 5):
        N7745C.write(f":SENSe{channel}:FUNCtion:STATe LOGG,STOP")

    # Fermer la connexion
    N7745C.close()
    rm.close()
