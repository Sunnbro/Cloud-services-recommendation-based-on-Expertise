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
comment = "I have been using Dreamweaver for many years, what is this preprocessing even about, i am wondering how it works."

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
