#!/usr/bin/env python3

# Pour manipuler le Systeme de Fichiers et les arguments en ligne de commande
import os
import sys

# Pour convertir des dates EXIF en objet dates
from datetime import datetime

# Pour lire lire les images et leurs metadonneees
from PIL import Image

# Pour traduire les codes EXIF en noms humains (comme 'DateTimeOriginal')
from PIL.ExifTags import TAGS



# La fonction qui recupere la date de prise de vue depuis le fichier image
def get_exif_date(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()

        if not exif_data:
            return None

        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)

            if tag_name == 'DateTimeOriginal':
                return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")

    except Exception as e:
        print(f"Erreur EXIF sur {file_path} : {e}")
    return None


# La fonction qui renomme le fichier
def rename_photos_by_date(directory):

    # initialisation d'un dictionnaire
    counter = {}

    # parcourt tout le dossier en recuperant la liste de tous les fichiers
    for filename in os.listdir(directory):

        # on construit le nom absolu du fichier
        file_path = os.path.join(directory, filename)

        if not os.path.isfile(file_path):
            continue

        # le nom de fichier termine pr jpg ou jpeg
        if not filename.lower().endswith(('.jpg', '.jpeg')):
            continue

        # appelle de la fonction sur chaque fichier
        date_taken = get_exif_date(file_path)

        if not date_taken:
            print(f"Date EXIF non trouvée pour : {filename}")
            continue

        # traduit les formats de date
        base_name = date_taken.strftime("%Y-%m-%d_%H-%M-%S")

        # nouveau nom de fichier horodate
        new_name = base_name + ".jpg"


        while os.path.exists(os.path.join(directory, new_name)):
            counter[base_name] = counter.get(base_name, 1) + 1
            new_name = f"{base_name}_{counter[base_name]}.jpg"

        new_path = os.path.join(directory, new_name)
        os.rename(file_path, new_path)
        print(f"Renommé : {filename} → {new_name}")



# Le programme principal
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python sorter.py /chemin/vers/dossier/photos")
        sys.exit(1)

    photos_dir = sys.argv[1]
    if not os.path.isdir(photos_dir):
        print("Erreur : le chemin fourni n'est pas un dossier.")
        sys.exit(1)

    rename_photos_by_date(photos_dir)

