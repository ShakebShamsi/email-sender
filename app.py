from email.message import EmailMessage
import ssl
import smtplib



email_sender = 'frenzyvader@gmail.com'
email_password = 'fxayobiwzbyurdum'

email_receiver ='thnshamsi@gmail.com'

subject = "Hello! This is Shakeb."
body = """
I am here to wish a very very very happy Eid.
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
