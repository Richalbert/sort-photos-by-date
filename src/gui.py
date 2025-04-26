import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import subprocess
import os
import smtplib
from email.mime.text import MIMEText
import json

class PhotoSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sort Photos by Date")

        self.folder_path = tk.StringVar()
        self.simulate = tk.BooleanVar()
        self.recipient_email = tk.StringVar()

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

        # Envoi par mail
        frame_email = tk.Frame(self.root)
        frame_email.pack(pady=5)
        tk.Label(frame_email, text="Envoyer les logs à :").pack(side=tk.LEFT)
        tk.Entry(frame_email, textvariable=self.recipient_email, width=30).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_email, text="Envoyer", command=self.send_logs_by_email).pack(side=tk.LEFT)

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

        cmd = ["python3", "sorter.py", folder]
        if simulate:
            cmd.append("--simulate")

        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            self.log_output.delete(1.0, tk.END)
            for line in process.stdout:
                self.log_output.insert(tk.END, line)
                self.log_output.see(tk.END)
        except Exception as e:
            messagebox.showerror("Erreur", str(e))


    def load_config(self):
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
                return config.get("email", {})
        except Exception as e:
            messagebox.showerror("Erreur config", f"Impossible de charger la config.json : {e}")
            return {}


    def send_logs_by_email(self):
        recipient = self.recipient_email.get().strip()
        if not recipient:
            messagebox.showerror("Erreur", "Veuillez entrer une adresse e-mail.")
            return

        log_content = self.log_output.get(1.0, tk.END).strip()
        if not log_content:
            messagebox.showinfo("Info", "Aucun log à envoyer.")
            return


        config = self.load_config()
        sender = config.get("sender")
        smtp_server = config.get("smtp_server")
        smtp_port = config.get("smtp_port")
        smtp_user = config.get("smtp_user")
        smtp_password = config.get("smtp_password")

        if not all([sender, smtp_server, smtp_port, smtp_user, smtp_password]):
            messagebox.showerror("Erreur", "Configuration email incomplete")
            return


        try:
            msg = MIMEText(log_content)
            msg["Subject"] = "Logs - Sort Photos by Date"
            msg["From"] = sender
            msg["To"] = recipient

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_password)
                server.send_message(msg)

            messagebox.showinfo("Succès", f"Logs envoyés à {recipient}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de l’envoi : {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoSorterApp(root)
    root.mainloop()

