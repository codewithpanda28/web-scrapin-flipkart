# Flipkart Scraper

This Python script scrapes product information such as **name**, **price**, **rating**, and **specifications** from Flipkart's search page for "phones under 15000" and saves the details into a CSV file.

## Requirements

- **Python 3.x** (Recommended version 3.7 or higher)
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`

## Installation

### Step 1: Install Python

Make sure Python 3.x is installed on your system. You can verify this by running the following command in your terminal:

```bash
python --version
```

If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Required Libraries

Install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4 pandas
```

### Step 3: Save the Script

Save the provided Python code into a file named `flipkart_scraper.py`.

### Step 4: Run the Script

After saving the script, open the terminal (or command prompt), navigate to the directory where the script is saved, and run the script using:

```bash
python flipkart_scraper.py
```

This will scrape the data from Flipkart and save it as a CSV file named `flipkart.csv`.

## Python Script

```python
from bs4 import BeautifulSoup
import requests
import pandas as pd

flipkart = {}

name_list, price_list, rating_list, specifications_list = [], [], [], []
info = [name_list, price_list, rating_list, specifications_list]

base_path = "https://www.flipkart.com"

for page in range(1, 2):  # Loop through 1 page
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
```

## Output

The script will create a file named `flipkart.csv` in the same directory. The CSV file will contain the following columns:
- **name**: The product name.
- **price**: The price of the product (in INR).
- **rating**: The rating of the product.
- **specifications**: A list of specifications for the product.

## Example Output

| name                                | price   | rating | specifications                                   |
|-------------------------------------|---------|--------|--------------------------------------------------|
| Xiaomi Redmi Note 10               | 13,999  | 4.3    | 6 GB RAM, 128 GB Storage, Snapdragon 678, 48 MP |
| Samsung Galaxy M32                  | 14,990  | 4.2    | 6 GB RAM, 128 GB Storage, 64 MP Camera          |
| Realme Narzo 30 Pro 5G              | 15,000  | 4.0    | 6 GB RAM, 128 GB Storage, 48 MP Camera          |

## Notes

- The script currently scrapes **1 page** of Flipkart's search results for "phones under 15000". To scrape more pages, modify the range in the loop.
- The script uses **requests** to fetch the webpage content and **BeautifulSoup** to parse the HTML.
- The scraped data is stored in a **Pandas DataFrame** and saved as a CSV file.

## Important Notes on Scraping

- Always check the website’s **robots.txt** and terms of service to ensure scraping is allowed.
- Too many requests in a short period could lead to your IP being blocked. Consider adding delays (e.g., using `time.sleep()`).

---

This version now includes the full Python code and all necessary steps.#
