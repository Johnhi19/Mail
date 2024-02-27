import smtplib, imaplib
from email.message import EmailMessage
import ssl
import email

file = open("assets/recipients.txt", "r")
recipients = file.read().split("\n")
sender = recipients[0]
receiver = recipients[1]
file.close()
file = open("assets/passwords.txt", "r")
pwd = file.read()
file.close()

body = "Hallo, \n ich teste gerade wie das funktioniert. \n LG Jojo"
subject = "Python-Mail :o"
context = ssl.create_default_context()

def send_email(subject, body, sender, receiver):
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp_server:
        smtp_server.login(sender, pwd)
        smtp_server.sendmail(sender, receiver, msg.as_string())
        smtp_server.quit()
    print('Message sent!')

def read_mail(receiver):
    with imaplib.IMAP4_SSL("imap.gmail.com", 993, ssl_context=context) as imap_server:
        imap_server.login(receiver, pwd)
        imap_server.select('inbox')
        response, messages = imap_server.search(None, 'Unseen')
        messages = messages[0].split()
        latest = int(messages[-1])
        oldest = int(messages[0])

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


if __name__=="__main__":
    #send_email(subject, body, sender, receiver)
    read_mail(sender)