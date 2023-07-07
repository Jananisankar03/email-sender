from email.message import EmailMessage
from a2 import password
import ssl
import smtplib

email_sender = 'senderemailid@gmail.com'
# generate app passwords in your Google account
email_password = password

email_receiver = 'receiveremailid@gmail.com'

subject = "Email subject"
body = """
Body of the email
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())