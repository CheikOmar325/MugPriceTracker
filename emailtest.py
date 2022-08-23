#I use this to test the email sending process before implementing in my code
import smtplib
import ssl
from email.message import EmailMessage

msg = EmailMessage()
#qtrtxazfkxljmwct
email_sender = 'quandeliciousdinglenut@gmail.com'
email_password = 'qtrtxazfkxljmwct'
email_receiver = 'kinas62519@ukgent.com'
subject = ('The item is on sale! Lets get this treasure!! ')
body = "Its on sale!"
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

