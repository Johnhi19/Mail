from flask import Flask, render_template, session, url_for, redirect, request
from emailServices import EmailService
import smtplib, imaplib

application = Flask(__name__)
service = EmailService()

@application.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('services.html')

@application.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['pwd']

        try:
            service.login(email, pwd)
            return redirect(url_for('services'))
        except:
            return "Failed to login. Please check your credentials and try again."
        
    return render_template('login.html')

@application.route('/services', methods=['POST', 'GET'])
def services():
    return render_template('services.html')

@application.route('/send_email', methods=['POST', 'GET'])
def send_email():
    if request.method == 'POST':
        receiver = request.form['receiver']
        subject = request.form['subject']
        body = request.form['body']
        service.send_email(subject, body, receiver)
        return redirect(url_for('services'))

    return render_template('send_email.html')

if __name__ == '__main__':
    application.run(debug=True)