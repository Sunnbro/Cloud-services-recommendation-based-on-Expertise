import json

# Ouvrir le fichier JSON
#with open('Software_5_Propre.json', 'r', encoding='utf-8') as file:
with open('Software_Complet_Propre.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

total_objects = len(data)

print("Nombre total d'objets :", total_objects)

count_with_vote = sum(1 for obj in data if "vote" in obj)

print("Nombre d'objets contenant 'vote' :", count_with_vote)
x = count_with_vote/total_objects
print("ratio :",x)
# Initialiser un dictionnaire pour stocker les votes par Asin
votes_par_asin = {}

# Parcourir les données pour compter les votes par Asin
for entry in data:
    asin = entry.get('asin')
    vote = entry.get('vote')
    if asin and vote:
        # Convertir le nombre de votes en entier
        vote = int(vote.replace(',', ''))
        votes_par_asin[asin] = votes_par_asin.get(asin, 0) + vote

# Trier les Asin par nombre de votes décroissant
sorted_asin = sorted(votes_par_asin.items(), key=lambda x: x[1], reverse=True)

# Afficher les 50 premiers Asin avec le plus grand nombre de votes
print("Les 50 premiers Asin avec le plus grand nombre de votes :")
for i, (asin, votes) in enumerate(sorted_asin[:50], 1):
    print(f"{i}. Asin: {asin}, Nombre de votes: {votes}")
