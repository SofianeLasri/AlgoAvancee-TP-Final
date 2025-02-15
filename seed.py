from database import db_session
from models import Tweet
from train_model import train_model


def seed_database():
    data = {
        "text": [
            "Je te déteste, tu es horrible !",
            "J'aime beaucoup cette vidéo, merci.",
            "Va te faire voir, imbécile.",
            "Quel contenu inspirant, bravo à l'équipe !",
            "Tu es vraiment nul et inutile.",
            "Je suis impressionné par la qualité de cette vidéo.",
            "Ferme-la, personne ne veut entendre ça.",
            "C'est une discussion constructive, merci pour vos efforts.",
            "Ce commentaire est complètement stupide et inutile.",
            "Merci pour cette vidéo, elle m'a beaucoup aidé !",
            "Personne n'a besoin de voir des bêtises pareilles.",
            "Excellent contenu, continuez comme ça !",
            "Tu ne comprends rien, arrête de commenter.",
            "Bravo, c'est exactement ce que je cherchais.",
            "Espèce d'idiot, tu ne sais même pas de quoi tu parles.",
            "Cette vidéo est très claire, merci pour le travail.",
            "Tu es une honte, personne ne veut lire ça.",
            "Le tutoriel est super bien expliqué, merci !",
            "C'est complètement débile, arrête de poster.",
            "J'adore cette chaîne, toujours des vidéos intéressantes.",
            "Dégage d'ici, personne ne te supporte.",
            "Merci pour ces conseils, c'est vraiment utile.",
            "T'es vraiment le pire, tes vidéos sont nulles.",
            "Une très bonne vidéo, claire et précise, bravo !"
        ],
        "label": [
            1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0
        ]}

    for i in range(len(data['text'])):
        tweet = Tweet(
            text=data['text'][i],
            positive=data['label'][i] == 0,
            negative=data['label'][i] == 1
        )
        db_session.add(tweet)
        db_session.commit()

    print("Now we have to train the model...")
    train_model()


def verify_database_has_tweets():
    tweets_count = Tweet.query.count()

    if tweets_count == 0:
        print("Database is empty. Populating with dummy data...")
        seed_database()
    else:
        print("Database already has tweets. Skipping population.")
