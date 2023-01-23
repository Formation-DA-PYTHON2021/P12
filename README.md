## Table des matières
* [Informations générales](#informations-générales)
* [Technologies utilisées](#technologies-utilisées)
* [Caractéristiques](#caractéristiques)
* [Installation](#installation)
* [Information](#information)
* [L'état du projet](#l-'-état-du-projet)
* [Auteurs](#auteurs)


## Informations générales

Projet 12 formation Open Classrooms : Développez une architecture back-end sécurisée en utilisant Django ORM.

## Technologies utilisées

Python - version 3.9.5

Django - version 4.1

PostgreSQL - pgAdmin4

Postman

## Caractéristiques

Refonte d'un logiciel de gestion de la relation client (CRM) interne et sécurisé.

## Installation 

Vous devez installer l'application "EpicEvents" disponible sur le lien : 
https://github.com/Formation-DA-PYTHON2021/P12.git

#### Récupération du projet : 

Copie dans un répértoire les éléments:

``git clone https://github.com/Formation-DA-PYTHON2021/P12.git``

#### Activer l'environnement virtuel : 

``cd P12``

``python -m venv env``

``source env\Scripts\activate``

#### Installer les paquets requis avec la commande : 

``pip install -r requirements.txt``

Attention il faudra ajouter package PostgresSQL si vous n'utilisez pas pgAdmin 4.

``pip install psycopg2``

#### Configuration Base de Données PostgreSQL:
- Installez [PostgreSQL](https://www.postgresql.org/download/). Ici vous trouverez la [documentation](https://www.postgresql.org/docs/).
- Créez une nouvelle base de données PostgreSQL avec SQL shell (psql) : 

``CREATE DATABASE your_db_name ``

#### Migration : 

- Vous devez ensuite migrer les données :

``py manage.py makemigrations``

``py manage.py migrate``

#### Démarage : 

- Lancer le serveur Django avec la commande : 

``python manage.py runserver``

- Dans le navigateur de votre choix, se rendre à l'adresse http://127.0.0.1:8000/


## Information 
Vous trouverez dans la documentation Postman toutes les informations necessaires : 
 - l'ensemble des points de terminaison de l'API, 
 - les permissions,
 - les fonctionnalités de l'API.

 La documentation Postman du projet est disponible sur le lien :

``https://documenter.getpostman.com/view/23674249/2s8ZDbVL9x``

Liste des utilisateurs existants :

| Nom           | Mot de Passe  |
| ------------- | ------------- |
| SuperUser     | S3cret!!      |
| ManagementUser| S3cret!!      |
| SalesUser     | S3cret!!      |
| SupportUser   | S3cret!!      |


## L'état du projet


Le projet est : complet


## Auteurs

T. CALVET
