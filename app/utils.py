# Project     : sort-photos-by-date
# File        : app/utils.py
# Date        : 2025-05-01
# Author      : Richalbert
# Version     : 1.0.0
# Description : Fonctions utilitaires pour l'application 
# Notes       : Version pour macOS


import os
import re
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS


def extract_exif_date(filepath):
    """
    Extrait la date de prise de vue depuis les métadonnées EXIF de la photo.
    Retourne une datetime formatee 'YYY-MM-DD_HH-MM-SS', ou None si non trouvée.
    """
    try:
        image = Image.open(filepath)
        exif_data = image._getexif()
        if not exif_data:
            return None

        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id)
            if tag == "DateTimeOriginal":
                return datetime.strptime(value, "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d_%H-%M-%S")
    except Exception as e:
        print(f"[ERREUR] EXIF non lisible pour {filepath} : {e}")
    return None


def format_filename(date_taken, counter=None, extension=".jpg"):
    """
    Génère un nom de fichier à partir d'une date (datetime) au format :
    YYYY-MM-DD_HH-MM-SS[_n].ext
    """
    base = date_taken.strftime("%Y-%m-%d_%H-%M-%S")
    if counter is not None:
        base += f"_{counter}"
    return base + extension.lower()


def get_file_extension(filepath):
    """
    Retourne l'extension du fichier, en minuscule, avec le point (ex: '.jpg').
    """
    return os.path.splitext(filepath)[1].lower()


def is_image_file(filename):
    """
    Vérifie si le fichier est une image (jpeg, png, etc.).
    """
    return bool(re.search(r"\.(jpe?g|png|gif|bmp|tiff?)$", filename, re.IGNORECASE))

