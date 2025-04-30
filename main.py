"""
Point d'entrée de l'application "Sort Photos by Date"
Lance l'interface graphique Tkinter
"""

import tkinter as tk
from app.gui import PhotoSorterApp


def main():
    root = tk.Tk()
    app = PhotoSorterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

