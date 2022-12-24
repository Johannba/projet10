# projet10

Projet réalisé dans le cadre de ma formation OpenClassrooms Développeur d'Applications Python.
Il s'agit d'une API réalisée avec Django pour une société fictive, SoftDesk.
L'application permet de remonter et suivre des problèmes techniques.

#  Caractéristiques
Tous les endpoints, leurs détails ainsi que des exemples d'utilisation sont décrits dans la documentation https://documenter.getpostman.com/view/24366090/2s8YzTViGo

# Installation et lancement
Commencez tout d'abord par installer Python.
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository :

```https://github.com/Johannba/projet12.git```

placez-vous dans le dossier projet10, puis créez un nouvel environnement virtuel 

``` pipenv install```

Ensuite, activez-le :

```pipenv shell```

Installez ensuite les packages requis :

```pip install -r requirements.txt```

Ensuite, placez vous à la racine du projet (là ou se trouve le fichier manage.py), puis effectuez les migrations :

```python manage.py makemigrations```

Alors :

```python manage.py migrate```

Il ne vous reste plus qu'à lancer le serveur :

```python manage.py runserver```

Vous pouvez ensuite utiliser l'application via les différents endpoints décrits dans la documentation. Vous devez d'abord créer un compte utilisateur à l'endpoint http://127.0.0.1:800/api/signup/ afin d'accéder aux fonctionnalités de l'application.





