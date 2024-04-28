import json

# Charger le fichier JSON
with open('C:/Users/Elitebook 845 G8/pythonprojects/Software_5_Propre.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Compter le nombre de fois que "asin": "0321719816" est présent dans le fichier
count = sum(1 for entry in data if entry.get('asin') == 'B00NG7JVSQ')

print("Nombre de fois que 'asin': '0321719816' est présent dans le fichier :", count)
