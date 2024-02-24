
from selenium import webdriver
from selenium.webdriver.common.by import By

URL="https://www.amazon.com.br/LG-32LQ620-Bluetooth-ThinQAI-compat%C3%ADvel/dp/B0B5HJYL3B/ref=sr_1_5?crid=3RW4SN431E48W"

driver = webdriver.Chrome()

driver.get(URL)

price_int_txt = driver.find_element(By.CLASS_NAME,'a-price-whole').text
price_int = int(price_int_txt.replace('.',""))
price_frac = float(driver.find_element(By.CLASS_NAME,'a-price-fraction').text)/100

print(price_int+price_frac)
driver.quit()