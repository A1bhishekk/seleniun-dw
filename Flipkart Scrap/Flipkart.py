import pandas as pd
import requests
from bs4 import BeautifulSoup
# import openpyxl
import smtplib
from email.message import EmailMessage
import glob
import numpy as np

Product_Name = []
Price = []
Description = []
Reviews = []


for i in range(1,50):
    url = 'https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=' + \
        str(i)

    r = requests.get(url)
    print(f"Extracting data from page no {i} of Flipkart Successfully")
    soup = BeautifulSoup(r.text, 'html.parser')
    box = soup.find('div', class_='_1YokD2 _3Mn1Gg')
    names = box.find_all('div', class_='_4rR01T')
    # print(names)
    for i in names:
        try:
            if i.text:
                Product_Name.append(i.text)
            else:
                Product_Name.append('-')
        except:
            # Product_Name.append('No Name')
            Product_Name.append(i.text)
        
       

    prices = box.find_all('div', class_='_30jeq3 _1_WHN1')

    for i in prices:
        try:
            Price.append(i.text)
        except:
            Price.append(np.nan)
       

    description = box.find_all('ul', class_='_1xgFaf')

    for i in description:
        try:
            Description.append(i.text)
        except:
            Description.append(np.nan)
        

    reviews = box.find_all('div', class_='_3LWZlK')

    for i in reviews:

        try:
            if i.text:
                Reviews.append(i.text)
            else:
                Reviews.append('-')
            # review = i.text
            # Reviews.append(review)
        except:
            Reviews.append(np.nan)


print(len(Product_Name),len(Price),len(Description),len(Reviews))
df = pd.DataFrame({'Product_Name': Product_Name, 'Price': Price,
                  'Description': Description,'Reviews': Reviews})
df.transpose()
df.to_csv('Flipkart2.csv', index=False)
# print(df.head())
# print(df.shape)


# send email with attachment
msg=EmailMessage()
msg['Subject']='Amazon Iphone web scraping'
msg['From']='Abhishek Kumar'
msg['To']='x4abhiop@gmail.com','sahniak9868@gmail.com'
# msg.set_content('This is a test email')
with open('Email.txt') as myfile:
    data=myfile.read()
    msg.set_content(data)

files=glob.glob('*.csv')
for file in files:
    with open(file,'rb') as f:
        file_data=f.read()
        file_name=f.name
        msg.add_attachment(file_data,maintype='application',subtype='csv',filename=file_name)



with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login('sahniak9868@gmail.com','eawbeidlglcmoiju')
    smtp.send_message(msg)

print("Email sent successfully 💕")





