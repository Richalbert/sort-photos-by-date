from setuptools import setup

APP = ['../../main.py']
DATA_FILES = ['../../config.json']
OPTIONS = {
    'argv_emulation': True,
    'includes': ['PIL', 'tkinter'],
    'packages': ['PIL'],
    'iconfile': 'app.icns',     # TODO icone
    'plist': {
        'CFBundleName': 'Sort Photos by Date',
        'CFBundleVersion': '1.0.0',
        'CFBundleIdentifier': 'com.richalbert.sortphotosbydate'
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

