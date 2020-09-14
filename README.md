# Site web de l'association ÉCLAT

Le site est en ligne à l'adresse https://eclat.ec-lyon.fr

## Contribuer du contenu En règle générale, s'inspirer [d'un article
existant](content/events/2019/2019-10-11-coffee_FR.md) et créer un fichier
Markdown.

Les en-têtes du fichier sont une partie importante qui permet de déterminer le
lien, la date, la langue de l'article, etc.

Généralement, consulter [la
documentation de pelican](https://docs.getpelican.com/en/stable/content.html).

## Développement

Si vous voulez tester vos changements localement avant de les soumettre, lisez
ce qui suit.

### Prérequis

Certains prérequis sont nécessaires
 * python 3
 * [pelican](https://blog.getpelican.com/): depuis les dépôts de votre
distribution Linux, ou `python -m pip install pelican` [voir
instructions](https://docs.getpelican.com/en/stable/install.html)
 * `make`
 * `lftp` si vous avez les identifiants pour mettre à jour le site

### Prévisualiser les changements

 1. Se placer dans le dossier du projet
 2. Lancer `make devserver`
 3. Dans votre navigateur, vous diriger vers http://127.0.0.1:8000 (vérifier
    qu'il s'agit de l'adresse montrée par la commande précédente).
 4. Faire vos modifications, sauvegardez, rechargez la page dans le navigateur.

### Envoyer les changements sur le serveur

Lancer `make ftp_upload`, et tapez le mot de passe. Il faut impérativement être
connecté au réseau local de l'ECL, ou au VPN.
