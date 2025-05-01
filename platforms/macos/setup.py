# Project     : sort-photos-by-date
# File        : platforms/macos/setup.py
# Date        : 2025-05-01
# Author      : Richalbert
# Version     : 1.0.0
# Description : Permet a py2app de packager l'application Python en une 
#               application .app native macOS
# Notes       : Version pour macOS

from setuptools import setup

APP = ['../../main.py']
DATA_FILES = ['../../config.json']
OPTIONS = {
    'argv_emulation': True,
    'includes': ['PIL', 'tkinter'],
    'packages': ['PIL'],
    'iconfile': 'app.icns',
    'plist': {
        'CFBundleName': 'Sort_Photos_by_Date',
        'CFBundleDisplayName': 'Sort_Photos_by_Date',
        'CFBundleVersion': '1.0.0',
        'CFBundleIdentifier': 'com.richalbert.sortphotosbydate',
        'CFBundleShortVersionString': '1.0',
        'LSMinimumSystemVersion': '10.13'
    }
}

setup(
    name='Sort_Photos_by_Date',
    description='Outil graphique pour trier et renommer des photos selon leur date de prise de vue (EXIF)',
    version='1.0',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

