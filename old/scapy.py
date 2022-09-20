from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
from selenium.webdriver.common.by import By

# Go to instagram login page

driver = webdriver.Chrome('G:\My Drive\Werk\BV\SEAM\Scraper\chomium\chromedriver_win32\chromedriver.exe')
driver.get('https://www.instagram.com/')

# Decline cookies
time.sleep(5)
cookies = driver.find_element(By.XPATH,  "//*[contains(text(), 'Only Allow Essential Cookies')]").click()

# Login in to your webbrowser
time.sleep(5)
username=driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password=driver.find_element(By.CSS_SELECTOR, "input[name='password']")
username.clear()
password.clear()
username.send_keys("Stuk_kompas")
password.send_keys("raakdewegkwijt!")
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Decline the password saving option
time.sleep(5)
save = driver.find_element(By.XPATH, "//*[contains(text(), 'Not now')]").click()

#Decline notifications
time.sleep(5)
notifications = driver.find_element(By.XPATH, "//*[contains(text(), 'Not Now')]").click()

# Go to page
time.sleep(5)

usernames='pickuplimes'

driver.get(f'https://www.instagram.com/{usernames}')
time.sleep(10)


followers = driver.find_element(By.XPATH, "//*[contains(text(), ' followers')]").get_attribute('innerHTML')
print(followers)

source = driver.page_source
data = bs(source, 'html.parser')

body = data.find('body')

# print(body)

# meta = re.findall(r'g,.=\ posts', str(body))

# ollowers = data.find("span", class_ = "g47SY ")
# span_followers = followers.find("span").text.strip()


