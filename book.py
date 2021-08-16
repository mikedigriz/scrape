import requests
from bs4 import BeautifulSoup
import pandas as pd

book_url = 'https://books.toscrape.com/catalogue/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
product_links = []
data = []

for _ in range(1, 3):
    req = requests.get(f'https://books.toscrape.com/catalogue/category/books/fantasy_19/page-{_}.html', headers=headers).text
    soup = BeautifulSoup(req, 'html.parser')
    product_list = soup.find_all('article', {'class': 'product_pod'})
    for product in product_list:
        link = product.find('a').get('href')
        product_links.append(book_url + link.replace('../../../', ''))

for link in product_links:
    req = requests.get(link, headers=headers).text
    bs_req = BeautifulSoup(req, 'html.parser')
    try:
        name = bs_req.find('h1').text.replace('\n', '')
    except:
        name = None
    try:
        description = bs_req.find('h2').find_next('p').text.replace('\n', '')
        print(description)
    except:
        description = None
    try:
        price = bs_req.find('p', {'class': 'price_color'}).text.replace('Â', '')
    except:
        price = None
    book = {'Название': name, 'Описание': description, 'Цена': price}
    data.append(book)
df = pd.DataFrame(data)
df.to_excel("fantasy_books.xlsx", index=False)

