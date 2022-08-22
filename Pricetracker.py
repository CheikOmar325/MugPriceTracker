# In this project I create a simple price tracker for a Persona 5 Mug

import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

URL = 'https://shopatlus.com/collections/persona-5-royal/products/magic-mug'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

Title = soup.find(itemprop='name', class_="product-single__title").get_text()
price = soup.find(id="ProductPrice-product-template").get_text()
float_price= float(price[1:])

print(Title,"", float_price)

#I will be setting up an email notification for when the mug's price changes
#In this version of the code the email sending feature has yet to be fully implemented
msg = EmailMessage()
def send_mail():
    msg ['Subject']= ("The item ", Title, 'is on sale for ', float_price)
    msg['From'] = 'The Phantom Thieves'
    msg['To'] = 'sakacheik@gmail.com'
    msg.set_content('test email from Joker')
    server= smtplib.SMTP_SSL("smtp@gmail.com", 465)

if (float_price == 16.99):
    print('Hey Joker! Your Mug is on sale! Lookin cool!')

