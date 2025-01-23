from bs4 import BeautifulSoup
import requests
import pandas as pd

demo = {}

name_list, price_list, rating_list, specifications_list = [], [], [], []
info = [name_list, price_list, rating_list, specifications_list]

base_path = "https://www.flipkart.com"

for page in range(1, 3):  # Loop through 10 pages
    url = f"https://www.flipkart.com/search?q=redmi+5g+mobile&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_7_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_7_na_na_na&as-pos=3&as-type=RECENT&suggestionId=redmi+5g+mobile&requestId=af8bdd6d-c455-47e6-a9a6-101820787ee3&as-backfill=on&page=2"
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
    demo[column] = inf

myData = pd.DataFrame(demo, columns=columns).to_csv('demo.csv', index=False)
print(myData)