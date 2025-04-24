# sort-photos-by-date

Script simple pour renommer automatiquement les fichiers photos selon leur date de prise de vue réelle (EXIF), afin qu'ils soient correctement triés sur tous les systèmes (Linux, macOS…).


## 🎯 Objectif

Réorganiser et renommer les fichiers `.jpg`/.`jpeg` dans un dossier en utilisant leur date réelle de capture, extraite des métadonnées EXIF.

Exemple de renommage :

IMG_1234.jpg -> 2025-04-25_00-14-22.jpg

En cas de doublous:

2025-04-25_00-14-22.jpg -> 2025-04-25_00-14-22_1.jpg -> ...


## 🚀 Utilisation

```bash
python sorter.py /chemin/vers/tes/photos

