# sort-photos-by-date

Script simple pour renommer automatiquement les fichiers photos selon leur date de prise de vue réelle (EXIF), afin qu'ils soient correctement triés sur tous les systèmes (Linux, macOS…).


## 🎯 Objectif

Réorganiser et renommer les fichiers `.jpg`/.`jpeg` dans un dossier en utilisant leur date réelle de capture, extraite des métadonnées EXIF.

Exemple de renommage :

IMG_1234.jpg -> 2025-04-25_00-14-22.jpg

En cas de doublons:

2025-04-25_00-14-22.jpg -> 2025-04-25_00-14-22_1.jpg -> ...


## Installation et environnement virtuel

1. Cloner le depot

git clone https://github.com/<ton-utilisateur>/sort-photos-by-date.git
cd sort-photos-by-date


2. Creer un environnement virtuel

python3 -m venv venv


3. Activer l'environnement

source venv/bin/activate


4. Installer les dependances

pip install -r requirements.txt





## 🚀 Utilisation

1. Tester en mode simulation

```bash
python sorter.py /chemin/vers/tes/photos --simulate






2. Appliquer les renommages

```bash
python sorter.py /chemin/vers/tes/photos

