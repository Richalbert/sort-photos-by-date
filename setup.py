from setuptools import setup

APP = ['src/gui.py']
DATA_FILES = [('config', ['src/config.json'])]
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PIL'],
    'iconfile': 'app.icns',     # TODO icone
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

