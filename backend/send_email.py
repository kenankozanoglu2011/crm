# backend/send_email.py

import smtplib
from email.message import EmailMessage
import pandas as pd

def send_event_emails(events):
    """
    events: liste halinde dict’ler; her dict’te en az 'email' anahtarı olmalı
    Örnek: [{'email': 'test@example.com', 'EventName': 'X', ...}, ...]
    """
    # SMTP sunucu bilgilerin (örneğin Gmail)
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587

    # Gönderen e-posta ve şifresi (veya app password)
    SENDER_EMAIL = "senin_email@gmail.com"
    SENDER_PASSWORD = "app_password_or_password"

    # Bağlantı kur
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)

    for record in events:
        recipient = record.get("email") or record.get("Email")  # sütun ismi neyse
        if not recipient:
            continue

        msg = EmailMessage()
        msg["Subject"] = "Event Notification"
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient

        # Mesaj içeriği; istersen etkinlik bilgilerini record’dan ekleyebilirsin
        event_name = record.get("EventName", "")
        msg.set_content(f"Hello,\n\nYou are invited to the event: {event_name}.\n\nBest regards.")

        server.send_message(msg)

    server.quit()
