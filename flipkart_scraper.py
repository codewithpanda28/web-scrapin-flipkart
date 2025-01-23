from bs4 import BeautifulSoup
import requests
import pandas as pd

flipkart = {}

name_list, price_list, rating_list, specifications_list = [], [], [], []
info = [name_list, price_list, rating_list, specifications_list]

base_path = "https://www.flipkart.com"

for page in range(1, 2):  # Loop through 10 pages
    url = f"https://www.flipkart.com/search?q=phone+under+15000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page}"
    response = requests.get(url)
    html_text = response.content
    soup = BeautifulSoup(html_text, 'html.parser')

    phones = soup.find_all('a', 'CGtC98')
    for phone in phones:
        name = phone.find('div', 'KzDlHZ').get_text()
        price = int(phone.find('div', 'Nx9bqj _4b5DiR').get_text().replace('₹', '').replace(',', ''))
        rating = 0 if (phone.find('div', 'XQDdHH') == None) else float(phone.find('div', 'XQDdHH').get_text())

        tags = phone.find_all('li', 'J+igdf')
        specifications = [li.get_text() for li in tags]

        detail = [name, price, rating, specifications]
        for inf, det in zip(info, detail):
            inf.append(det)

columns = ['name', 'price', 'rating', 'specifications']
for column, inf in zip(columns, info):
    flipkart[column] = inf

myData = pd.DataFrame(flipkart, columns=columns).to_csv('flipkart.csv', index=False)
print(myData)