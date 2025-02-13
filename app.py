import os

from flask import Flask, request, jsonify
from flask.cli import load_dotenv

import seed
from database import init_db

load_dotenv()

app = Flask(__name__)

db_config = {
    'host': os.getenv('DATABASE_HOST'),
    'user': os.getenv('MYSQL_DATABASE'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

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
    data = request.get_json()
    tweets = data['tweets']

    seed.verify_database_has_tweets()

    result = {}
    for i in range(len(tweets)):
        tweet_index = "tweet" + str(i)
        result[tweet_index] = 0.5

    return jsonify(result)


if __name__ == '__main__':
    app.run()
