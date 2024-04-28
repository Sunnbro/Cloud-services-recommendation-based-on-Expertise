import json

# Charger le fichier JSON
#with open('C:/Users/Elitebook 845 G8/pythonprojects/Software_5_Propre.json', 'r', encoding='utf-8') as file:
with open('C:/Users/Elitebook 845 G8/pythonprojects/Software_Complet_Propre.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initialiser un dictionnaire pour stocker le nombre total de votes pour chaque asin
votes_par_asin = {}

# Parcourir chaque avis dans le fichier JSON
for entry in data:
    asin = entry.get('asin')
    vote = entry.get('vote')

    # Vérifier si l'asin et le vote existent
    if asin and vote:
        # Supprimer la virgule de la chaîne de vote et la convertir en entier
        cleaned_vote = int(vote.replace(',', ''))
        
        # Ajouter le vote au total correspondant à cet asin
        votes_par_asin[asin] = votes_par_asin.get(asin, 0) + cleaned_vote

# Trouver l'asin avec le plus grand nombre total de votes
asin_max_votes = max(votes_par_asin, key=votes_par_asin.get)
nombre_votes_max = votes_par_asin[asin_max_votes]

print("L'asin avec le plus grand nombre total de votes est :", asin_max_votes)
print("Nombre total de votes :", nombre_votes_max)
