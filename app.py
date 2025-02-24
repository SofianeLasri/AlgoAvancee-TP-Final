import os
import re
import joblib
from flask import Flask, request, jsonify
from flask.cli import load_dotenv

import seed
from database import init_db, db_session
from models import Tweet
from train_model import train_model

load_dotenv()

app = Flask(__name__)

db_config = {
    'host': os.getenv('DATABASE_HOST'),
    'user': os.getenv('MYSQL_DATABASE'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# Je sais pas comment créer des commentaires similaires aux PhpDoc en Python mais on va faire comme ça :)
# Nous n'acceptons que des requêtes POST donnant un objet JSON ayant cette structure :
# { "tweets": [ "tweet content", "tweet content", "tweet content", ... ] }
# La réponse sera un objet JSON ayant cette structure (score entre -1 et 1) :
# { "tweet1": score1, "tweet2": score2, "tweet3": score3, ... }
@app.route('/analyze', methods=['POST'])
def analyze():
    init_db()
    seed.verify_database_has_tweets()

    data = request.get_json()

    if not data or 'tweets' not in data or not isinstance(data['tweets'], list):
        return jsonify({"error": "Invalid format!"}), 400

    model = joblib.load('positive_model.joblib')
    vectorizer = joblib.load('vectorizer.joblib')

    cleaned = [clean_text(t) for t in data['tweets']]
    transformed_tweets = vectorizer.transform(cleaned)
    probas = model.predict_proba(transformed_tweets)[:, 1]
    scores = {f"tweet{i}": float(2 * p - 1) for i, p in enumerate(probas)}

    for i, tweet in enumerate(data['tweets']):
        tweet = Tweet(
            text=tweet,
            positive=scores[f"tweet{i}"] > 0,
            negative=scores[f"tweet{i}"] < 0
        )
        db_session.add(tweet)
        db_session.commit()

    return jsonify(scores)


if __name__ == '__main__':
    app.run()
