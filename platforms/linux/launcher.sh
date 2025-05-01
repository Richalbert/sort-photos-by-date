#!/bin/bash

# Active l'environnement virtuel si présent
if [ -d "../../sortphotos-venv" ]; then
    source ../../sortphotos-venv/bin/activate
fi

# Change le dossier courant vers la racine du projet
cd ../../

# Lancer l'application Python
python3 main.py

