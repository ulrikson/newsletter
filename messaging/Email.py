import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import os
from dotenv import load_dotenv

load_dotenv()


class Email:
    def __init__(self, html):
        self.subject = "Goooob morning!"
        self.sender = "erik.ulrikson@gmail.com"
        self.receiver = "erik.ulrikson@gmail.com"
        self.html = html
    
    def send(self):
        message = Mail(from_email=self.sender, to_emails=self.receiver, subject=self.subject, html_content=self.html)
        try:
            sendgrid = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
            response = sendgrid.send(message)
            print(response.status_code)
        except Exception as e:
            print(e.message)

    def sendViaMailtrap(self):
        message = self.createMessage()

        with smtplib.SMTP(os.getenv("EMAIL_SERVER"), os.getenv("EMAIL_PORT")) as server:
            server.login(os.getenv("EMAIL_LOGIN"), os.getenv("EMAIL_PASSWORD"))
            server.sendmail(self.sender, self.receiver, message.as_string())

    def createMessage(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.sender
        message["To"] = self.receiver

        content = MIMEText(self.html, "html")
        message.attach(content)

        return message
