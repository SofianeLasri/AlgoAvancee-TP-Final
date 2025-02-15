import re

from joblib import dump
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

from database import db_session
from models import Tweet

french_stopwords = [
    "le", "la", "les", "un", "une", "des", "du", "de", "dans", "et", "en", "au",
    "aux", "with", "ce", "ces", "pour", "par", "sur", "pas", "plus", "où", "mais",
    "ou", "donc", "ni", "car", "ne", "que", "qui", "quoi", "quand", "à", "son",
    "sa", "ses", "ils", "elles", "nous", "vous", "est", "sont", "cette", "cet",
    "aussi", "être", "avoir", "faire", "comme", "tout", "bien", "mal", "on", "lui"
]

def train_model():
    print("Training model...")
    tweets = db_session.query(Tweet).all()

    texts = [clean_text(tweet.text) for tweet in tweets]
    labels = [1 if tweet.positive else 0 for tweet in tweets]

    vectorizer = CountVectorizer(stop_words=french_stopwords, max_features=100)
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression()
    model.fit(X, labels)

    dump(model, 'model.joblib')
    dump(vectorizer, 'vectorizer.joblib')
    print("Model trained and saved to disk.")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text