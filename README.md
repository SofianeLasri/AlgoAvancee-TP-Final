# TP final d'algorithmique avancée

## Installation

Il est nécessaire d'avoir Docker installé sur votre machine.

Pour lancer le projet, il suffit de lancer la commande suivante :

```bash
docker-compose up
```

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