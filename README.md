# TP final d'algorithmique avancée

## Installation

Il est nécessaire d'avoir Docker installé sur votre machine.

Pour lancer le projet, il suffit de copier le .env d'exemple et de lancer la commande suivante :

```bash
docker-compose up
```

Un cron se lance une fois par semaine pour entrainer le modèle.

## Utilisation

Le projet est accessible à l'adresse suivante : [http://localhost:5000](http://localhost:5000)

Seule l'adresse /analyze est accessible. Elle acceptes les requêtes POST contenant du JSON ayant ce format :

```json
{
    "tweets": ["Tu est affreux !", "Il faut beau aujourd'hui."]
}
```

**Exemple de réponse :**

```json
{
    "tweet0": -0.3583773813818951,
    "tweet1": 0.009870971954487606
}
```

## Notes techniques

Le projet utilise MariaDB pour stocker les données. Voici le fichier env à copier afin de lancer le projet :

```env
FLASK_ENV=development
DATABASE_HOST=db
DATABASE_PORT=3306

MYSQL_ROOT_PASSWORD=password
MYSQL_DATABASE=flask
MYSQL_USER=flask-user
MYSQL_PASSWORD=password
```

L'ORM utilisé est SQLAlchemy.