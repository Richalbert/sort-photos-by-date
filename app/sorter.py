# Project     : sort-photos-by-date
# File        : app/sorter.py
# Date        : 2025-05-01
# Author      : Richalbert
# Version     : 1.0.0
# Description : Gere le tri et le renommage des photos 
#               utilise les metadonnees EXIF
#               Fonctionne avec un callback de log et affichage dans l'interface
# Notes       : Version pour macOS


import os
import shutil
from datetime import datetime
from app.utils import extract_exif_date 


def sort_photos(directory, simulate=False, log_callback=print):
    """
    Trie et renomme les photos dans un répertoire en fonction de leur date EXIF.
    - simulate : si True, affiche les actions sans les exécuter.
    - log_callback : fonction pour afficher les messages (ex: print ou zone de texte GUI).
    """
    if not os.path.isdir(directory):
        log_callback(f"❌ Le dossier '{directory}' n'existe pas ou n'est pas valide.")
        return

    log_callback(f"📂 Dossier sélectionné : {directory}")
    renamed_count = 0
    errors = 0

    for filename in os.listdir(directory):
        original_path = os.path.join(directory, filename)

        if not os.path.isfile(original_path):
            continue

        extension = os.path.splitext(filename)[1].lower()
        if extension not in [".jpg", ".jpeg", ".png"]:
            log_callback(f"⏭️ Fichier ignoré (non-image) : {filename}")
            continue

        exif_date = extract_exif_date(original_path)
        if not exif_date:
            log_callback(f"⚠️ Pas de date EXIF pour {filename}")
            errors += 1
            continue

        new_name = f"{exif_date}{extension}"
        new_path = os.path.join(directory, new_name)
        counter = 1

        while os.path.exists(new_path):
            new_name = f"{exif_date}_{counter}{extension}"
            new_path = os.path.join(directory, new_name)
            counter += 1

        if simulate:
            log_callback(f"[Simulation] {filename} → {new_name}")
        else:
            try:
                shutil.move(original_path, new_path)
                #log_callback(f"✅ {filename} renommé en {new_name}")
                log_callback(f"[Renommage] {filename} → {new_name}")
                renamed_count += 1
            except Exception as e:
                log_callback(f"❌ Erreur avec {filename} : {e}")
                errors += 1

    log_callback(f"\n✔️ Opération terminée. {renamed_count} renommé(s), {errors} erreur(s).\n")

