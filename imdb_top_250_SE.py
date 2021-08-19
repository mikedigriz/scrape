from bs4 import BeautifulSoup
from selenium import webdriver

option = webdriver.ChromeOptions()
# option.add_argument('--headless')
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome('C:/Users/admin/Downloads/chromedriver/chromedriver.exe', options=option)
driver.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(driver.page_source, 'html.parser')


links = soup.select('td.titleColumn a')
films = links[:250]
count = 0

for _ in films:
    count += 1
    print(f'{count}. ' + _.text)
