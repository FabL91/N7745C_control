# Définir les variables pour le pas et la valeur finale

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s', filename='test_list.log', encoding='utf-8', level=logging.DEBUG)

pas_tps = 10
nbre_pts = 100

# Créer la liste de temps
temps = list(range(0, nbre_pts + 1, pas_tps))  # On ajoute 1 à valeur_finale pour inclure la valeur finale

# Afficher la liste pour vérification
print(temps)
logger.info(temps)
