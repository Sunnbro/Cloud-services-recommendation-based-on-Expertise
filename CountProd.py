import json

# Charger le fichier JSON
with open('C:/Users/Elitebook 845 G8/pythonprojects/Software_Complet_Propre.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Créer un ensemble pour stocker les ASIN uniques
unique_asins = set()

# Parcourir les données et ajouter chaque ASIN à l'ensemble
for entry in data:
    asin = entry.get('asin')
    if asin:
        unique_asins.add(asin)

# Nombre d'ASIN uniques
unique_count = len(unique_asins)

print("Nombre d'ASIN uniques dans le fichier :", unique_count)
