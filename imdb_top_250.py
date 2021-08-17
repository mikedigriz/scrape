import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
page = requests.get('https://www.imdb.com/chart/top/', headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
links = soup.select('td.titleColumn a')
films = links[:250]
count = 0

for _ in films:
    count += 1
    print(f'{count}. ' + _.text)
