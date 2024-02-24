from selenium import webdriver
from selenium.webdriver.common.by import By

URL="https://www.python.org/"

driver = webdriver.Chrome()

driver.get(URL)

# search_bar = driver.find_element(By.ID, 'id-search-field')
# print(search_bar.tag_name)

# logo = driver.find_element(By.CLASS_NAME, 'python-logo')
# print(logo.size)

about = driver.find_element(By.XPATH,'//*[@id="container"]/li[1]/a')
print(about.text)

driver.quit()