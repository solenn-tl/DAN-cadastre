# DAN

## Documentation
* [Documentation](https://atr.pages.teklia.com/dan/)
* [Dépôt DAN Teklia (privé)](https://gitlab.teklia.com/atr/dan)

## Installation
0. Créer un environnement virtuel (activer avec ```source .venv/bin/activate```)
1. Installer Nerval : ```pip install nerval-master.tar.gz```
2. Installer DAN : ```pip install dan-main.zip```

## Pré-requis
* Python >= 3.10
* Base de données SQLITE extraite d'Arkindex contenant les annotations (!! sets obligatoirement nommés train/val/test)

## Phases
### Création des sets d'entraînement
* ```00-create_train_val_test.ipynb```
### Préparation des données d'entrainement
* ```10-prepare-data-dan.ipynb```
### Entrainement
* ```20-train-dan.ipynb```
### Evaluation 
* ```30-evaluation-dan.ipynb```
* ```31-fix-parallel-training-troubles.ipynb``` : *préparation du modèle pour l'inférence (si entrainement réalisé avec sur plusieurs GPU)*
### Inference
* ```40-inference-dan.ipynb```

## Aide
* Lancer tensorboard ```tensorboard --logdir output --bind_all``` dans le dossier où sont contenus les résultats du modèle (ex: ```outputs/train_110324```)
TEST
## Questions
- Lignes ou pages pour la création dataset : https://doc.callico.eu/campaigns/export/arkindex/#also-export-entities-on-a-parent-extra-field-for-entity-form-campaigns
- Taille du vocabulaire 