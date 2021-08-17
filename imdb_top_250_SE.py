from bs4 import BeautifulSoup
from selenium import webdriver

option = webdriver.ChromeOptions()
# option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
driver = webdriver.Chrome('C:/Users/admin/Downloads/chromedriver/chromedriver.exe', options=option)
driver.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(driver.page_source, 'html.parser')


links = soup.select('td.titleColumn a')
films = links[:250]
count = 0

for _ in films:
    count += 1
    print(f'{count}. ' + _.text)
