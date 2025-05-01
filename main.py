"""
Point d'entrée de l'application "Sort Photos by Date"
Lance l'interface graphique Tkinter
"""

import tkinter as tk
from app.gui import PhotoSorterApp

import platform

def main():

    system = platform.system()

    if system == "Darwin":
        print("macOS detecte")
    elif system == "Linux":
        print("Linux detecte")
    else:
        print("Systeme inconnu")

    root = tk.Tk()
    app = PhotoSorterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

