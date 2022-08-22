#I use this to test the email sending process before implementing in my code
import smtplib
from email.message import EmailMessage
msg = EmailMessage()

msg ['Subject']= ('The item is on sale! Lets get this treasure!! ')
msg['From'] = 'The Phantom Thieves'
msg['To'] = 'sakacheik@gmail.com'
msg.set_content('test email from Joker')
server = smtplib.SMTP_SSL("smtp@gmail.com", 465)
server.login('quandeliciousdinglenut@gmail.com','mdp12345')
server.send_message(msg)
server.quit()