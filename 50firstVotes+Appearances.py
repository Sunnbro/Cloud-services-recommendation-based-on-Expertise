import json

# Ouvrir le fichier JSON
with open('Software_Complet_Propre.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initialiser un dictionnaire pour stocker les votes par Asin
votes_par_asin = {}
appearances = {}

# Parcourir les données pour compter les votes par Asin et le nombre d'apparitions
for entry in data:
    asin = entry.get('asin')
    vote = entry.get('vote')
    if asin and vote:
        # Convertir le nombre de votes en entier
        vote = int(vote.replace(',', ''))
        votes_par_asin[asin] = votes_par_asin.get(asin, 0) + vote
        appearances[asin] = appearances.get(asin, 0) + 1

# Trier les Asin par nombre de votes décroissant
sorted_asin = sorted(votes_par_asin.items(), key=lambda x: x[1], reverse=True)

# Afficher les 50 premiers Asin avec le plus grand nombre de votes et leur nombre d'apparitions
print("Les 50 premiers Asin avec le plus grand nombre de votes et leur nombre d'apparitions:")
for i, (asin, votes) in enumerate(sorted_asin[:50], 1):
    count = appearances.get(asin, 0)
    print(f"{i}. Asin: {asin}, Votes: {votes}, Count: {count}")
