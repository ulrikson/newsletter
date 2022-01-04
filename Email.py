import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()

#! Code needs refactoring

class Email:
    def __init__(self):
        self.port = 2525
        self.smtp_server = "smtp.mailtrap.io"
        self.login = os.getenv("MAILTRAP_LOGIN")
        self.password = os.getenv("MAILTRAP_PASSWORD")
    
    def sendEmail(self):
        sender_email = "mailtrap@example.com"
        receiver_email = "new@example.com"

        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email

        # write the plain text part
        text = """\
        Hi,
        Check out the new post on the Mailtrap blog:
        SMTP Server for Testing: Cloud-based or Local?
        /blog/2018/09/27/cloud-or-local-smtp-server/
        Feel free to let us know what content would be useful for you!"""
        
        # write the HTML part
        html = """\
        <html>
        <body>
            <p>Hi,<br>
            Check out the new post on the Mailtrap blog:</p>
            <p><a href="/blog/2018/09/27/cloud-or-local-smtp-server">SMTP Server for Testing: Cloud-based or Local?</a></p>
            <p> Feel free to <strong>let us</strong> know what content would be useful for you!</p>
        </body>
        </html>
        """
        
        # convert both parts to MIMEText objects and add them to the MIMEMultipart message
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        
        # send your email
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.login(self.login, self.password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        
        print('Sent') 

Email().sendEmail()