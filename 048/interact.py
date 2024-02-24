from selenium import webdriver
from selenium.webdriver.common.by import By

URL="https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome()

driver.get(URL)

# article_count = int(driver.find_element(By.ID, 'articlecount').text.split()[0].replace(',',''))
article_count = int(driver.find_element(By.CSS_SELECTOR, '#articlecount a').text.replace(',',''))
print(article_count)

driver.quit()