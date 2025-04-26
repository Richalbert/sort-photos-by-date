#!/bin/bash

echo "Nettoyage ancien build..."
rm -rf build/ dist/

echo "Création de l'environnement virtuel..."
python3 -m venv venv
source venv/bin/activate

echo "Installation des dépendances..."
pip install -r requirements.txt
pip install py2app

echo "Construction de l'application Mac (.app)..."
python setup.py py2app

echo "Terminé ! L'application est dans le dossier dist/"

