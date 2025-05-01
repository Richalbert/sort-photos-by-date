"""
Module: gui
Description: Interface graphique de l'application "Sort Photos by Date"
Auteur: Richard + ChatGPT
Date: 2025
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from app.sorter import sort_photos  # Fonction principale
from app.mailer import send_log_email


class PhotoSorterApp:
    """
    Classe principale de l'application GUI.
    Gère l'interface et les interactions utilisateur.
    """

    def __init__(self, root):
        """
        Initialise l'application et ses variables.
        """
        self.root = root
        self.root.title("Sort Photos by Date")

        # Variables
        self.directory_path = tk.StringVar()
        self.simulate = tk.BooleanVar(value=True)
        self.logs = []

        # Crée toute l'interface
        self.setup_ui()

    def setup_ui(self):
        """
        Construit l'interface graphique.
        """
        # Choix du dossier
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(fill=tk.X)

        tk.Label(frame, text="Répertoire à trier :").pack(side=tk.LEFT)
        tk.Entry(frame, textvariable=self.directory_path, width=50).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Parcourir", command=self.browse_directory).pack(side=tk.LEFT)

        # Mode simulation
        sim_frame = tk.Frame(self.root, padx=10, pady=5)
        sim_frame.pack(fill=tk.X)
        tk.Checkbutton(sim_frame, text="Simulation (ne renomme pas réellement)", variable=self.simulate).pack(anchor='w')

        # Boutons d'action
        action_frame = tk.Frame(self.root, padx=10, pady=10)
        action_frame.pack(fill=tk.X)
        #tk.Button(action_frame, text="Lancer le tri", command=self.run_sorting).pack(side=tk.LEFT)
        tk.Button(action_frame, text="Lancer le tri", command=self.run_sorting).pack(pady=(5,10))

        # Zone d'affichage des logs
        log_frame = tk.Frame(self.root, padx=10, pady=10)
        log_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(log_frame, text="Logs :").pack(anchor='w')
        self.log_text = ScrolledText(log_frame, height=12, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)

        self.email_button = tk.Button(self.root, text="Envoyer les logs par email", command=self.send_logs_by_email)
        self.email_button.pack(pady=(5,10))

    def browse_directory(self):
        """
        Ouvre un sélecteur de dossier pour choisir le répertoire contenant les photos.
        """
        path = filedialog.askdirectory()
        if path:
            self.directory_path.set(path)

    def run_sorting(self):
        """
        Lance le tri des photos avec ou sans simulation.
        """
        path = self.directory_path.get()
        if not os.path.isdir(path):
            messagebox.showerror("Erreur", "Répertoire invalide.")
            return

        self.log_text.delete(1.0, tk.END)  # Nettoie les logs précédents
        self.logs = []

        def log_callback(message):
            self.logs.append(message)
            self.log_text.insert(tk.END, message + "\n")
            self.log_text.see(tk.END)

        try:
            sort_photos(path, simulate=self.simulate.get(), log_callback=log_callback)
            messagebox.showinfo("Succès", "Tri terminé.")
        except Exception as e:
            log_callback(f"Erreur : {e}")
            messagebox.showerror("Erreur", str(e))

    def send_logs_by_email(self):
        """
        Envoie les logs par email 
        """
        logs = self.log_text.get("1.0", tk.END).strip()

        if not logs:
            messagebox.showinfo("Aucun log", "Aucun log à envoyer.")
            return

        try:
            send_log_email(logs)
            messagebox.showinfo("Email envoyé", "Les logs ont été envoyés.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'envoyer les logs :\n{e}")


