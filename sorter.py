import os
import sys
import argparse
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

def get_exif_date(file_path):
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data is not None:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    if tag == 'DateTimeOriginal':
                        return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Erreur EXIF pour {file_path} : {e}")
    return None

def generate_new_name(date_taken, ext, existing_names):
    base_name = date_taken.strftime("%Y-%m-%d_%H-%M-%S")
    new_name = f"{base_name}{ext}"
    counter = 1
    while new_name in existing_names:
        new_name = f"{base_name}_{counter}{ext}"
        counter += 1
    return new_name

def sort_photos(directory, simulate=False):
    if not os.path.isdir(directory):
        print(f"Le dossier '{directory}' n'existe pas.")
        return

    print(f"{'Simulation de' if simulate else 'Début du'} tri des photos dans : {directory}\n")

    files = os.listdir(directory)
    existing_names = set()
    for filename in files:
        filepath = os.path.join(directory, filename)
        if not os.path.isfile(filepath):
            continue

        ext = os.path.splitext(filename)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png']:
            continue

        date_taken = get_exif_date(filepath)
        if not date_taken:
            print(f"[IGNORÉ] Pas de date trouvée pour : {filename}")
            continue

        new_name = generate_new_name(date_taken, ext, existing_names)
        new_path = os.path.join(directory, new_name)
        existing_names.add(new_name)

        if simulate:
            print(f"[SIMULATION] {filename} -> {new_name}")
        else:
            try:
                os.rename(filepath, new_path)
                print(f"[RENOMMÉ] {filename} -> {new_name}")
            except Exception as e:
                print(f"[ERREUR] Échec renommage de {filename} : {e}")

    print("\nTri terminé.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trier les photos par date EXIF.")
    parser.add_argument("directory", help="Répertoire contenant les photos")
    parser.add_argument("--simulate", action="store_true", help="Simuler le renommage (aucun changement)")
    args = parser.parse_args()

    sort_photos(args.directory, simulate=args.simulate)

