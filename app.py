from flask import Flask, request

app = Flask(__name__)


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
    data = request.get_json()
    tweets = data['tweets']

    result = {}
    for i in range(len(tweets)):
        tweetIndex = "tweet" + str(i)
        result[tweetIndex] = 0.5

    return result


if __name__ == '__main__':
    app.run()
