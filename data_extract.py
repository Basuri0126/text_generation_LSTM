import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

driver.get('https://www.gutenberg.org/')
time.sleep(5)

user_input = driver.find_element(by=By.XPATH, value='//*[@id="menu-book-search"]')
user_input.send_keys('the scarlet letter')
time.sleep(2)

user_input.send_keys(Keys.ENTER)
time.sleep(2)

link = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[2]/div/ul/li[4]')
link.click()
time.sleep(2)

link2 = driver.find_element(by=By.XPATH, value='//*[@id="download"]/div/table/tbody/tr[2]/td[2]/a')
link2.click()
time.sleep(11)

html_code = driver.page_source

page_soup = BeautifulSoup(html_code, 'lxml')

paragraphs = page_soup.find_all('p')

content = ' '.join([para.get_text(strip=True) for para in paragraphs])
with open('data_extract.txt', 'w', encoding='utf-8') as file:
    file.write(content)



