from selenium import webdriver
from selenium.webdriver.common.by import By

URL="https://www.python.org/"

driver = webdriver.Chrome()

driver.get(URL)

# search_bar = driver.find_element(By.ID, 'id-search-field')
# print(search_bar.tag_name)

# logo = driver.find_element(By.CLASS_NAME, 'python-logo')
# print(logo.size)

# about = driver.find_element(By.XPATH,'//*[@id="container"]/li[1]/a')
# print(about.text)

event_dates = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')

events = {}

for n in range(len(event_dates)):
    events[n] = {
        "date" : event_dates[n].text,
        "name" : event_names[n].text
    }
    

print(events)

driver.quit()