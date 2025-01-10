# Reconnaissance automatique du texte manuscrit dans les registres cadastraux

1. Transcription structurée des tableaux d'états de sections
2. Structuration fine des colonnes complexes (adresses, contribuables) à l'aide de LLM (création de dataset)

## Documentation
### DAN
* [Dépôt DAN Teklia](https://gitlab.teklia.com/atr/dan)
* [Documentation DAN](https://atr.pages.teklia.com/dan/)
* [Dépôt Nerval Teklia](https://gitlab.teklia.com/ner/nerval)
### Ollama
* [Ollama](https://ollama.com/)

## Installation
1. Créer un environnement virtuel :
- ```cd DAN-cadastre```
- ```python3 -m venv .venv_dan```

2. Activer l'environnement : 
    * ```source .venv_dan/bin/activate```
    * ```.venv_dan/bin/activate```

3. Exécuter ```setup.sh``` pour installer Nerval et DAN :
    * ```chmod +x setup.sh```
    * ```./setup.sh```

## Pré-requis
* Python >= 3.10
* Base de données SQLITE extraite d'Arkindex contenant les annotations (!! sets obligatoirement nommés train/val/test)
* Ollama

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

## Questions
- Lignes ou pages pour la création dataset : https://doc.callico.eu/campaigns/export/arkindex/#also-export-entities-on-a-parent-extra-field-for-entity-form-campaigns
- Taille du vocabulaire 

## Attention
* Le token spécial § est utilisé dans mes annotations mais est aussi utilisé dans NERVAL comme séparateur.