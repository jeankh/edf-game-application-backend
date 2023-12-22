from email.mime.text import MIMEText
import smtplib

def send_email( recipient):
   subject="Test"
   body=  "This is a test email"   
   sender="coursemates39@gmail.com"
   password="qdvz ouvu zvyx akge"
   msg = MIMEText(body)
   msg['Subject'] = subject
   msg['From'] = sender
   msg['To'] = recipient
   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
      smtp_server.login(sender, password)
      smtp_server.sendmail(sender, recipient, msg.as_string())
   print("Message sent!")