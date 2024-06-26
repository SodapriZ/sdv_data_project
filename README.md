# Projet de Tableau de Bord E-commerce - MaxiCoffee

## Introduction

MaxiCoffee souhaite rendre l'univers du café accessible à tous, en offrant des expériences de partage, de connaissances et de dégustation.
Url du site : https://www.maxicoffee.com/

## Objectif du Projet

Construire un tableau de bord e-commerce en suivant ces étapes :
1. **Collecte des données** : Utiliser BeautifulSoup pour extraire des données d'un site e-commerce et une API pour obtenir des informations complémentaires.
2. **Traitement des données** : Nettoyer et transformer les données pour les rendre exploitables.
3. **Stockage des données** : Sauvegarder les données nettoyées dans un fichier CSV ou JSON.
4. **Analyse des données** : Extraire des informations utiles comme les statistiques descriptives et les produits populaires.
5. **Visualisation des données** : Utiliser des bibliothèques comme Matplotlib et Seaborn pour créer des graphiques.

## Prérequis

Assurez-vous d'avoir Python installé sur votre machine :

```sh
python --version
```

## Installation
1. **Clonez le dépôt du projet :**

```sh
git clone https://github.com/votre-utilisateur/votre-projet.git
cd votre-projet
```
2. **Créez et activez un environnement virtuel :**

- Sur Windows :
```sh
python -m venv .venv
.venv\Scripts\activate
```
 - Sur macOS/Linux :
```sh
Copier le code
python -m venv .venv
source .venv/bin/activate
```
3. **Installez les dépendances :**

```sh
pip install -r requirements.txt
```

## Exécution :
Pour executer le serveur mongodb :
```sh
docker-compose up
```

Ajouter le mongo-spark-connector.jar disponible dans ./extra dans le dossier .venv/lib/site-packages/pyspark/jars/

Pour exécuter le script principal :
```sh
python .\app\main.py
```

## Contributeurs :
- Leonie COLY
- Galdos GOUDJO
- Anatole PECULIER
