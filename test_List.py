# Définir les variables pour le pas et la valeur finale
pas_tps = 10
nbre_pts = 100

# Créer la liste de temps
temps = list(range(0, nbre_pts + 1, pas_tps))  # On ajoute 1 à valeur_finale pour inclure la valeur finale

# Afficher la liste pour vérification
print(temps)