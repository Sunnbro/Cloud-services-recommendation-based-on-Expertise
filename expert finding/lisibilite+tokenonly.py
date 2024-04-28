import readability
import nltk

# Téléchargez les données nltk nécessaires pour la tokenisation
nltk.download('punkt')

# Texte à analyser
text = "The ability to turn your spoken communication into text is an admirable goal."

# Tokenisation du texte
tokens = nltk.word_tokenize(text)

# Convertir les tokens en une seule chaîne pour la bibliothèque readability
tokenized_text = ' '.join(tokens)

# Obtenir les mesures de lisibilité
results = readability.getmeasures(tokenized_text, lang='en')
print(results['readability grades']['FleschReadingEase'])
