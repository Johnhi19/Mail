import smtplib, imaplib
from email.message import EmailMessage
import ssl
import email

def login(sender, pwd):
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp_server:
                smtp_server.login(sender, pwd)
        except:
            raise AssertionError(f"Failed to login for {sender}")
    
login("bla", "as")