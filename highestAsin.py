import json
from collections import Counter

# Chemin vers le fichier JSON
#json_file_path = "C:/Users/Elitebook 845 G8/pythonprojects/Software_5_Propre.json"
json_file_path = "C:/Users/Elitebook 845 G8/pythonprojects/Software_Complet_Propre.json"

# Ouvrir le fichier JSON
with open(json_file_path, "r") as file:
    # Charger les données JSON
    data = json.load(file)

# Extraire les valeurs "asin" dans une liste
asin_values = [entry.get("asin") for entry in data]

# Compter le nombre d'occurrences de chaque valeur "asin"
asin_counts = Counter(asin_values)

# Trouver la valeur "asin" avec le plus grand nombre d'occurrences
most_common_asin = asin_counts.most_common(1)[0]

print("La balise 'asin' la plus fréquente est :", most_common_asin)
