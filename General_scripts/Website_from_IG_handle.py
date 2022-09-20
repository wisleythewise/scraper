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



#importing usernames 
handles = pd.read_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/orderchampSocials.csv")

# Placeholder for usernames
# followers = []
websites = []


for handle in handles['instagramLinks']:
    # print("this is the handle", handle)

    username = handle.replace('@', '')

    # try: 
    #     driver.get(f'https://www.instagram.com/{username}')
    #     time.sleep(5)
    #     followers_element = driver.find_element(By.XPATH, "//*[contains(text(), ' followers')]").get_attribute('innerHTML')
    #     data = bs(followers_element, 'html.parser')
    #     followers.append(data.text)
    # except: 
    #     followers.append("error loading followers")

    try: 
        driver.get(handle)
        time.sleep(5)
        website = driver.find_element(By.CSS_SELECTOR, "div[class='_7UhW9    vy6Bb       qyrsm   tx0Md            fDxYl    T0kll ']").text
        websites.append(website)
    except: 
        websites.append("error loading websitis")

    # print lists 
    # print(followers)
    print(websites)

    


# export only the handles
# followers = {'followers' : followers}
# backup = pd.DataFrame(followers)
# backup.to_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/faireMerchantFollowers.csv")

# export only the handles
websitesMerchant = {'websites' : websites}
backup = pd.DataFrame(websitesMerchant)
backup.to_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/orderchampwebsites.csv")


