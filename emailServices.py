import smtplib, imaplib
from email.message import EmailMessage
import ssl
import email

class EmailService:
    def __init__(self):
        self.context = ssl.create_default_context()

    def send_email(self, subject, body, sender, receiver, pwd):
        msg = EmailMessage()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context) as smtp_server:
            smtp_server.login(sender, pwd)
            smtp_server.sendmail(sender, receiver, msg.as_string())
            smtp_server.quit()
        print('Message sent!')

    def read_mail(self, receiver, pwd):
        with imaplib.IMAP4_SSL("imap.gmail.com", 993, ssl_context=self.context) as imap_server:
            imap_server.login(receiver, pwd)
            imap_server.select('inbox')
            response, messages = imap_server.search(None, 'Unseen')
            messages = messages[0].split()
            latest = int(messages[-1])

            for i in range(latest, latest-5, -1):
                data = imap_server.fetch(str(i), '(RFC822)')
                for response_part in data:
                    arr = response_part[0]
                    if isinstance(arr, tuple):
                        msg = email.message_from_bytes(arr[1])

                        print("date", msg['Date'], "\n")
                        print("From: " + msg['from'] + "\n")
                        print("Subject: " + msg['subject'] + "\n")

                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                body = part.get_payload(decode=True)
                                print("Body: \n" + body.decode('utf-8') + "\n")
                        print("-"*100)

            imap_server.close()