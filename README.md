# Sort Photos by Date


**Description :**
Application simple pour trier des photos par date de prise de vue a partir de metadonnees EXIF
Fonctionne sur **Linux** et **MacOS** (bientot Android)

---

## Fonctionnalites principales

- Tri automatique des photos par daste/heure reelle
- Renommage des fichiers selon un format standarise
- Simulation du tri sans modifier les fichiers
- Interface graphique (Tjinter)
- Export et envoi des logs par mail

---


## Instructions pour construire l'application sur macOS

1. Cloner ce dépôt

<code>
    git clone https://github.com/Richalbert/sort-photos-by-date.git
    cd sort-photos-by-date
</code>

2. Creer un environnement virtuel

<code>
    python3 m venv sortphotos-venv
    source sortphotos-venev/bin/activate
</code>

3. Installer les dependances

<code>
    pip install -r requirements.txt
</code>

4. Lancer l'application

<code>
    python gui.py
</code>

---

2bis. Exécuter le script `build.sh`
3bis. L'application `.app` sera disponible dans le dossier `dist/`

---

## Dépendances

- Python 3
- Pillow
- py2app


---

## TODO

- Support Android
- Chiffrement securise de la configuration


---

## Licence

Projet sous licence MIT
