# In this project I create a simple price tracker for a Persona 5 Mug

import requests
from bs4 import BeautifulSoup
import smtplib
import ssl
from email.message import EmailMessage

URL = 'https://shopatlus.com/collections/persona-5-royal/products/magic-mug'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/104.0.0.0 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

Title = soup.find(itemprop='name', class_="product-single__title").get_text()
price = soup.find(id="ProductPrice-product-template").get_text()
float_price = float(price[1:])

print(Title, "", float_price)

# I will be setting up an email notification for when the mug's price changes
# In this version of the code the email sending feature has yet to be fully implemented
msg = EmailMessage()


def send_mail():
    msg = EmailMessage()
    # qtrtxazfkxljmwct
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


if float_price < 16.99:
    print('Hey Joker! Your Mug is on sale! Lookin cool!')
    send_mail()
elif float_price > 16.99:
    print('The Price got raised')
    send_mail()
