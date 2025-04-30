"""
app/mailer.py

Contient la fonction d'envoi d'email pour transmettre les logs de l'application.
Utilise smtplib et email.message.
"""

import smtplib
from email.message import EmailMessage
import json
from pathlib import Path

# Chemin vers le fichier de configuration
CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.json"

def load_config():
    """
    Charge les parametres SMTP depuis le fichier config.json
    """
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Fichier de configuration json introuvable : {CONFIG_PATH}")

    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def send_log_email(log_content):
    """
    Envoie un email contenant les logs a l'adresse configuree"
    """
    config = load_config()
    smtp_server = config["smtp"]["server"]
    smtp_port = config["smtp"]["port"]
    smtp_user = config["smtp"]["user"]
    smtp_password = config["smtp"]["password"]
    recipient = config["smtp"]["recipient"]

    msg = EmailMessage()
    msg["Subject"] = "Logs de l'application - sort-photos-by-date"
    msg["From"] = smtp_user
    msg["To"] = recipient
    msg.set_content(log_content)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

