""" Day 051 - SpeedTest + Twiter """

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

URL_SPEEDTEST = "https://www.speedtest.net/"
PROMISSE_DOWN = 150.0
PROMISSE_UP = 10.0
TWITTER_EMAIL = ""
TWITTER_PASS = ""

class InternetSpeedTwiterBot():
    """ Class for this project """
    def __init__(self):
        self.down = 0.0
        self.up = 0.0
        self.driver = webdriver.Chrome()

    def get_internet_speed(self):
        """ Get the internet Speed (down and up)"""
        self.driver.get(URL_SPEEDTEST)
        sleep(2)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        sleep(40)
        down_txt = self.driver.find_element(By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = float(down_txt)
        up_txt = self.driver.find_element(By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = float(up_txt)

        self.driver.quit()


    def tweet_at_provider(self):
        """Send a tweetter to ISP complaining about speed"""
        print("Your connection is below of you have contracted")
        print(f"You contracted {PROMISSE_DOWN} Mbps of Download, but they're providing only {internet_speed.down} Mbps")


# main()
internet_speed = InternetSpeedTwiterBot()

internet_speed.get_internet_speed()

if internet_speed.down < PROMISSE_DOWN or internet_speed.up < PROMISSE_UP:
    internet_speed.tweet_at_provider()
    