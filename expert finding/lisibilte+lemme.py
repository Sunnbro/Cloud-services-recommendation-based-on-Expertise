import readability
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import spacy

# Télécharger les ressources nécessaires pour NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')  
nltk.download('words')

# Initialiser le lemmatizer et le stemmer
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Initialiser le modèle de langue spaCy
nlp = spacy.load('en_core_web_sm')

# Exemple de commentaire
comment = ("The ability to turn your spoken communication into text is an admirable goal.  Unfortunately Dragon Naturally Speaking Premium 11, even after a few hours of \"training\" (both of myself and the software) the effort required to produce a few lines of incorrectly transcribed English made this product seem much more like \"obstacle\" than \"aid\".\n\nYes, I tried the plug in headset that comes with the software.  Yes, I also tried the microphone that works perfectly for skyping and magic-jack phone calls. Yes, I spent two hours interfacing with the machine, reading prepared text back to the software and \"teaching\" it corrections to the mistakes it was making. No, I don't speak with a lisp or use English as a third language after being raised in China or Eastern Europe.\n\nThis product would only be recommended for those who are not fluent with a keyboard, or who wouldn't mind scads of errors in their text.\n\nI'm not giving up on the prospect that suitable software may exist in the future, compatible with common PC set-ups.  Truth in advertising: I received my copy gratis as an Amazon Vine Voice reviewer.  Obtained free, I still do not use this product.")


# Tokenization avec NLTK
tokens = word_tokenize(comment.lower())

# Lemmatization avec NLTK
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

# Stemming avec NLTK
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Lemmatization avec spaCy
doc = nlp(comment.lower())
lemmatized_tokens_spacy = [token.lemma_ for token in doc]

print("Tokens après lemmatisation (NLTK):", lemmatized_tokens)
print("Tokens après stemming (NLTK):", stemmed_tokens)
print("Tokens après lemmatisation (spaCy):", lemmatized_tokens_spacy)

# Convertir les tokens en une seule chaîne pour la bibliothèque readability
tokenized_text = ' '.join(lemmatized_tokens_spacy)

# Obtenir les mesures de lisibilité
results = readability.getmeasures(tokenized_text, lang='en')
print(results['readability grades']['FleschReadingEase'])