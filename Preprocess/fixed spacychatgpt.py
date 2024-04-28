import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Chargement du modèle Spacy
nlp = spacy.load("en_core_web_sm")

# Fonction de prétraitement
def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
    return " ".join(tokens)

# Exemple de texte
#text = "Though not without its faults, this software is amazingly accurate."
text = "Though not without its faults, this software is amazingly accurate.\n\nI haven't tried voice recognition software in a long time, mainly because it used to take a lot of \"training\" (reading hour-long passages of text while the software learns my speech patterns) to get it to an acceptable level of accuracy.  A lot has changed in the last several years: improvements in voice recognition algorithms, and more powerful home computers have led to software that is impressively accurate right out of the box.  In under five minutes of reading to my computer, I found that the software was giving me near-perfect accuracy.  As a test, I read Walt Whitman's poem, \"When I Heard the Learn'd Astronomer\".  I read at a very natural pace (perhaps even a bit rushed), including punctuation, and the software scored 100% for accuracy.\n\nBesides its accuracy, Dragon NaturallySpeaking impressed me with its fairly intuitive set of commands, both for editing documents and for \"getting around\" in Windows and on the web.  Though references are provided to let you know the commands that are available, I found it pretty easy to guess correctly at the commands I needed.  For example, I said, \"search the web for computer science\".  A browser window quickly opened, and took me to the Bing search page to show me the results for \"computer science\".  Preferring Google results, I decided to try \"Search Google for computer science\".  Sure enough, it worked to (as did searching Yahoo).  Then I tried \"search computer for jpegs\" and immediately was presented with a list of jpeg files on my computer.  When I'm not sure what to say, I just need to say \"What can I say\", and Dragon NaturallySpeaking will give me a list of commands.  (And, apparently, I can teach it new commands, but I haven't tried that yet.)  All in all, I found that I could guess the right commands about 75% of the time.\n\nA NOTE ABOUT MULTIPLE USERS: I found it interesting that the software recognized my own voice almost perfectly, but when I handed the microphone over to my 11-year-old son, the accuracy dropped to about zero percent.  Apparently, those five minutes I spent reading must have helped it \"lock in\" to my voice and speech patterns.  I wondered if it would be possible to set up a separate profile for my son.  As far as I can tell, however, the license for this software is bound to \"an individual\".  You, the user, can use the software (even on multiple machines, though not simultaneously).  However, multiple people cannot use the software on one machine unless each gets a license.  Please note that this is my understanding of the license agreement.  Don't trust my interpretation.  If you intend to allow multiple people to use the software, you may want to investigate the exact terms of the license.\n\nOne other issue: the installation process was a bit bumpy for me on my Windows 7 Professional 64-bit edition.  And, once installed, I had trouble downloading the free update from version 11 to version 11.5.  However, customer service was helpful in sending me steps to correct the issue.  Now that it's installed and updated, I find it to work very well, and is very unobtrusive.\n\nAll in all, I'm very happy with this latest version of Dragon NaturallySpeaking, and expect that it will get a lot of use!"
# Prétraitement du texte
preprocessed_text = preprocess(text)

# Création d'un corpus
corpus = [preprocessed_text]

# Création de la matrice TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

# Recherche des termes les plus importants
feature_names = vectorizer.get_feature_names_out()
scores = tfidf_matrix.toarray()[0]
top_indices = scores.argsort()[-5:][::-1]
top_keywords = [feature_names[i] for i in top_indices]

# Affichage des termes les plus importants
print("Top keywords:", top_keywords)
