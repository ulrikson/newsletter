import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()


class Email:
    def __init__(self, text, html):
        self.subject = "Daily newsletter!"
        self.sender = "mailtrap@example.com"
        self.receiver = "erik.ulrikson@gmail.com"
        self.text = text
        self.html = html

    def send(self):
        message = self.createMessage()

        with smtplib.SMTP(os.getenv("EMAIL_SERVER"), os.getenv("EMAIL_PORT")) as server:
            server.login(os.getenv("EMAIL_LOGIN"), os.getenv("EMAIL_PASSWORD"))
            server.sendmail(self.sender, self.receiver, message.as_string())

    def createMessage(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.sender
        message["To"] = self.receiver

        part1 = MIMEText(self.text, "plain")
        part2 = MIMEText(self.html, "html")
        message.attach(part1)
        message.attach(part2)

        return message
