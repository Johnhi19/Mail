import smtplib, imaplib
from email.message import EmailMessage
import ssl

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
        imap_server.select()
        typ, data = imap_server.search(None, 'ALL')
        for num in data[0].split():
            typ, data = imap_server.fetch(num, '(RFC822)')
            print('Message %s\n%s\n' % (num, data[0][1]))

        imap_server.close()
        imap_server.logout()


if __name__=="__main__":
    #send_email(subject, body, sender, receiver)
    read_mail(sender)