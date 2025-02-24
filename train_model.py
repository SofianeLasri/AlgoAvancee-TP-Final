import re

from joblib import dump
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

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
    # labels = [1 if tweet.positive else 0 for tweet in tweets]

    positive_labels = [1 if tweet.positive else 0 for tweet in tweets]
    negative_labels = [1 if tweet.negative else 0 for tweet in tweets]

    vectorizer = CountVectorizer(stop_words=french_stopwords, max_features=100)
    X_positive = vectorizer.fit_transform(texts)
    X_negative = vectorizer.fit_transform(texts)
    Y_positive = positive_labels
    Y_negative = negative_labels

    X_train_positive, X_test_positive, y_train_positive, y_test_positive = train_test_split(X_positive, Y_positive, test_size=0.2, random_state=42)
    X_train_negative, X_test_negative, y_train_negative, y_test_negative = train_test_split(X_negative, Y_negative, test_size=0.2, random_state=42)

    positive_model = LogisticRegression()
    negative_model = LogisticRegression()

    positive_model.fit(X_train_positive, y_train_positive)
    negative_model.fit(X_train_negative, y_train_negative)

    dump(positive_model, 'positive_model.joblib')
    dump(negative_model, 'negative_model.joblib')
    dump(vectorizer, 'vectorizer.joblib')

    print("Model trained and saved to disk.")

    print("-- DEBUG --")
    y_pred_positive = positive_model.predict(X_test_positive)
    y_pred_negative = negative_model.predict(X_test_negative)

    print("Rapport de classification du modèle positif :")
    print(classification_report(y_test_positive, y_pred_positive))

    print("Matrice de confusion du modèle positif :")
    print(confusion_matrix(y_test_positive, y_pred_positive))

    print("Rapport de classification du modèle négatif :")
    print(classification_report(y_test_negative, y_pred_negative))

    print("Matrice de confusion du modèle négatif :")
    print(confusion_matrix(y_test_negative, y_pred_negative))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text