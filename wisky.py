import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://www.thewhiskyexchange.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
product_links = []
data = []
for _ in range(1, 6):
    req = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={_}&psize=24&sort=pasc', headers=headers).text
    soup = BeautifulSoup(req, 'html.parser')
    product_list = soup.find_all('li', {'class': 'product-grid__item'})
    for product in product_list:
        link = product.find('a', {'class': 'product-card'}).get('href')
        product_links.append(baseurl + link)

for link in product_links:
    req_price = requests.get(link, headers=headers).text
    bs_req_prise = BeautifulSoup(req_price, 'html.parser')
    try:
        price = bs_req_prise.find('p', {'class': 'product-action__price'}).text.replace('\n', '')
    except:
        price = None
    try:
        about = bs_req_prise.find('div', {'class': 'product-main__description'}).text.replace('\n', '')
    except:
        about = None
    try:
        rating = bs_req_prise.find('div', {'class': 'review-overview'}).text.replace('\n', '')
    except:
        rating = None
    try:
        name = bs_req_prise.find('h1', {'class': 'product-main__name'}).text.replace('\n', '')
    except:
        name = None
    whisky = {'Виски': name, 'Цена': price, 'Рейтинг': rating, 'Описание': about}
    data.append(whisky)
df = pd.DataFrame(data)
df.to_excel("wisky.xlsx", index=False)
