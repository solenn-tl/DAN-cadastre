# DAN

## Documentation
* [Documentation DAN](https://atr.pages.teklia.com/dan/)
* [Dépôt DAN Teklia](https://gitlab.teklia.com/atr/dan)

## Installation
0. Créer un environnement virtuel (activer avec ```source .venv/bin/activate```)
1. Installer Nerval : ```pip install nerval-master.tar.gz``` ([télécharger ici](https://gitlab.teklia.com/ner/nerval))
2. Installer DAN : ```pip install dan-main.zip``` ([télécharger ici](https://gitlab.teklia.com/atr/dan))

## Pré-requis
* Python >= 3.10
* Exemple de JSON produit à partir d'annotations Arkindex (split.json)
* Exemple de fichier de configuration de l'entrainement (config1.json)

## Phases
### Préparation des données d'entrainement
* ```10-prepare-data-dan.ipynb```
### Entrainement
* ```20-train-dan.ipynb```
### Evaluation 
* ```30-evaluation-dan.ipynb```
### Inference
* ```40-inference-dan.ipynb```

## Suivi des métriques
* Lancer tensorboard ```tensorboard --logdir output --bind_all``` dans le dossier où sont contenus les résultats du modèle (ex: ```outputs/train_110324```)