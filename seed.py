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
            "Une très bonne vidéo, claire et précise, bravo !",
            "Cette vidéo est une vraie perte de temps.",
            "Merci pour cette astuce, ça m'a sauvé la vie !",
            "Tu ne devrais même pas essayer de parler, c'est ridicule.",
            "Bravo pour cette démonstration claire et utile.",
            "Ce contenu est tellement mauvais, c'est affligeant.",
            "J'ai appris énormément grâce à cette vidéo, merci !",
            "Tu es juste jaloux, tes commentaires sont pathétiques.",
            "Superbe travail, continuez comme ça !",
            "C'est un désastre, tu devrais avoir honte.",
            "Merci pour votre aide, c'était très clair.",
            "Arrête de poster des trucs aussi nuls, c'est insupportable.",
            "Cette chaîne est une vraie mine d'or, bravo !",
            "Ton avis est inutile et stupide, arrête de parler.",
            "J'ai adoré cette vidéo, elle est parfaite.",
            "Tu es vraiment une personne toxique, c'est triste.",
            "Merci pour ce contenu de qualité, c'est génial.",
            "C'est le pire truc que j'ai vu de ma vie.",
            "Grâce à vous, j'ai enfin compris, merci !",
            "Tu es complètement à côté de la plaque, arrête.",
            "C'est exactement ce dont j'avais besoin, merci beaucoup !",
            "Ton commentaire est tellement bête qu'il en est drôle.",
            "Merci pour votre travail, c'est toujours un plaisir.",
            "Tu devrais vraiment réfléchir avant de poster des choses pareilles.",
            "Une explication claire et concise, bravo !",
            "C'est tellement mauvais que ça en devient comique.",
            "Merci pour cette vidéo, elle m'a ouvert les yeux.",
            "Tu es la raison pour laquelle Internet est toxique.",
            "Excellent travail, je recommande cette chaîne à tout le monde.",
            "Arrête de faire perdre du temps aux gens avec tes absurdités.",
            "Merci pour cette vidéo, elle est très inspirante.",
            "Tu es un clown, personne ne t'écoute.",
            "Un contenu de grande qualité, comme toujours.",
            "C'est une honte de poster des choses aussi mauvaises.",
            "Merci pour cette leçon, c'était très enrichissant.",
            "Tu es pathétique, arrête de te ridiculiser.",
            "Une vidéo parfaite pour comprendre le sujet, merci !",
            "C'est tellement stupide que ça en devient gênant.",
            "Merci pour cette explication, c'était très clair.",
            "Tu es une perte de temps incarnée.",
            "Bravo pour cette vidéo, elle est exceptionnelle."
        ],
        "label": [
            1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
            1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0
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
