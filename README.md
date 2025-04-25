# sort-photos-by-date

Script simple pour renommer automatiquement les fichiers photos selon leur date de prise de vue réelle (EXIF), afin qu'ils soient correctement triés sur tous les systèmes (Linux, macOS…).
avec interface graphique minimaliste qui selectionne le dossier photos + simulation + bouton tri + affiche les logs

Exemple de renommage :

IMG_1234.jpg -> 2025-04-25_00-14-22.jpg

En cas de doublons:

2025-04-25_00-14-22.jpg -> 2025-04-25_00-14-22_1.jpg -> ...


## Installation et environnement virtuel

### 1. Cloner le depot
<code>
git clone https://github.com/Richalbert/sort-photos-by-date.git
cd sort-photos-by-date
</code>

### 2. Creer un environnement virtuel
<code>
python3 -m venv venv
</code>

### 3. Activer l'environnement
<code>
source venv/bin/activate
</code>

### 4. Installer les dependances
<code>
pip install -r requirements.txt
</code>


## 🚀 Utilisation

### 1. Tester en mode simulation

<code>
python sorter.py /chemin/vers/tes/photos --simulate
</code>

### 2. Appliquer les renommages

<code>
python sorter.py /chemin/vers/tes/photos
</code>
