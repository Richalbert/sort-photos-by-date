#!/usr/bin/env python3

import os
import sys
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

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

def rename_photos_by_date(directory, simulate=False):
    counter = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if not os.path.isfile(file_path):
            continue
        if not filename.lower().endswith(('.jpg', '.jpeg')):
            continue

        date_taken = get_exif_date(file_path)
        if not date_taken:
            print(f"Date EXIF non trouvée pour : {filename}")
            continue

        base_name = date_taken.strftime("%Y-%m-%d_%H-%M-%S")
        new_name = base_name + ".jpg"
        while os.path.exists(os.path.join(directory, new_name)):
            counter[base_name] = counter.get(base_name, 1) + 1
            new_name = f"{base_name}_{counter[base_name]}.jpg"

        new_path = os.path.join(directory, new_name)
        if simulate:
            print(f"[SIMULATION] {filename} → {new_name}")
        else:
            os.rename(file_path, new_path)
            print(f"Renommé : {filename} → {new_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage : python sorter.py /chemin/vers/dossier/photos [--simulate]")
        sys.exit(1)

    photos_dir = sys.argv[1]
    simulate = "--simulate" in sys.argv

    if not os.path.isdir(photos_dir):
        print("Erreur : le chemin fourni n'est pas un dossier.")
        sys.exit(1)

    rename_photos_by_date(photos_dir, simulate)

