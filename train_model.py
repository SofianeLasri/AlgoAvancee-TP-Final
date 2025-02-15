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

    for tweet in tweets:
        print(tweet.text + " - " + str(tweet.positive) + " - " + str(tweet.negative))