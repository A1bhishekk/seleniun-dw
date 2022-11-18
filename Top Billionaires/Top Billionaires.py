import pandas as pd
import requests
from bs4 import BeautifulSoup

url='https://www.bloomberg.com/billionaires'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())
names = soup.find_all('div', class_='table-cell active t-nw')
print(names)
for i in names:
    print(i.text)
