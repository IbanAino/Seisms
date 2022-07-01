# Outil de saisie des mesures absolues

**Auteur :** Iban FERNANDEZ

**Date :** 2022

Cet outil est dédié à l'analiste des données sismiques qui doit consulter les séismes journalier mondiaux.

![Alt text](rsc_doc/graphical_interface.png?raw=true "Interface")

## Installation

Tous les fichiers doivent être copiés ensembles dans un même répertoire :
- Seisms.py
- Model.py
- View.py
- Controller.py
- config.txt
- README.md
- rsc_doc/*

Modules Python3 supplémentaires à télécharger :
- **tkinter** : affichage graphique
- **configparser** : lire des fichiers de configuration
- **re** : utiliser les expressions régulières
- **datetime** : définir la date du jour

```bash:
sudo apt-get install python3-tk
pip install configparser
pip install regex
pip install datetime
```

## Configuration

Avant la première utilisation il convient d'éditer le fichier de configuration config.txt

Ce fichier contient les coordonnées géogpahiques de la station à partir de laquelle calculer la distance au séisme.

Ce fichier contient également les proxys pour se connecter à internet.


## Utilisation

Pour lancer le logiciel, lancer le fichier Saisir.py avec Python3 (en se plaçant dans le répertoire du fichier):

```bash:
python3 Seisms.py
```
