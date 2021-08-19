from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd


options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome('/home/misha/chromedriver/chromedriver/chromedriver', options=options)
driver.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(driver.page_source, 'html.parser')
links = soup.select('td.titleColumn a')
films = links[:10]
final_scraped_info = []
for _ in films:
    driver.get('https://imdb.com/' + _['href'])
    infolist = driver.find_element_by_css_selector('.ipc-inline-list')
    informations = infolist.find_elements_by_css_selector('[role=presentation]')
    scraped_info = {
        'Название': _.text,
        'Год': informations[0].text,
        'Продолжительность': informations[2].text
    }
    final_scraped_info.append(scraped_info)
df = pd.DataFrame(final_scraped_info)
df.to_excel('Films.xlsx')
print(df)
