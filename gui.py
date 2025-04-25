import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import subprocess
import os

class PhotoSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sort Photos by Date")

        # Répertoire sélectionné
        self.folder_path = tk.StringVar()

        # Checkbox simulation
        self.simulate = tk.BooleanVar()

        # Interface
        self.setup_ui()

    def setup_ui(self):
        # Choix du dossier
        frame_path = tk.Frame(self.root)
        frame_path.pack(pady=10)
        tk.Label(frame_path, text="Dossier de photos :").pack(side=tk.LEFT)
        tk.Entry(frame_path, textvariable=self.folder_path, width=50).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_path, text="Parcourir", command=self.browse_folder).pack(side=tk.LEFT)

        # Case simulation
        tk.Checkbutton(self.root, text="Mode simulation (ne renomme pas)", variable=self.simulate).pack(pady=5)

        # Bouton de traitement
        tk.Button(self.root, text="Lancer le tri", command=self.run_sorter).pack(pady=5)

        # Zone de log
        self.log_output = scrolledtext.ScrolledText(self.root, width=80, height=20)
        self.log_output.pack(padx=10, pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def run_sorter(self):
        folder = self.folder_path.get()
        simulate = self.simulate.get()

        if not folder or not os.path.isdir(folder):
            messagebox.showerror("Erreur", "Veuillez sélectionner un dossier valide.")
            return

        # Commande Python
        cmd = ["python3", "sorter.py", folder]
        if simulate:
            cmd.append("--simulate")

        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            self.log_output.delete(1.0, tk.END)
            for line in process.stdout:
                self.log_output.insert(tk.END, line)
                self.log_output.see(tk.END)

        except Exception as e:
            messagebox.showerror("Erreur", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoSorterApp(root)
    root.mainloop()

