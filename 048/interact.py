from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL="https://en.wikipedia.org/wiki/Main_Page"

URL="http://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Chrome()

driver.get(URL)

# article_count = int(driver.find_element(By.ID, 'articlecount').text.split()[0].replace(',',''))
#article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')

#print({int(article_count.text.replace(',',''))})
#article_count.click()
#contents_portals = driver.find_element(By.LINK_TEXT, 'Contents portals')


# icone_btn = driver.find_element(By.XPATH, '//*[@id="p-search"]/a')
# icone_btn.click()

# search = driver.find_element(By.NAME, 'search')
# search.send_keys("Python")
# search.submit()

# time.sleep(3)
# contents_portals.click()

first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys("Joaquim")

last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys("Silva")

email = driver.find_element(By.NAME, 'email')
email.send_keys("joaquim.silva@exeample.com")

submit_bt = driver.find_element(By.CLASS_NAME, 'btn' )
submit_bt.click()

time.sleep(4)

driver.quit()