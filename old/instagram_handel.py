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

#Get that session
# Go given page
driver = webdriver.Chrome('G:\My Drive\Werk\BV\SEAM\Scraper\chomium\chromedriver_win32\chromedriver.exe')

driver.get("https://www.faire.com/?utm_source=bing&utm_medium=cpc&utm_campaign=SEM_BI_EMEA_NL___RTL_BR___BMM&keyword=faire&matchtype=e&creative=&device=c&msclkid=897158ecf4ec13513b313ad7cae9d345")
time.sleep(5)

# Logging in
notifications = driver.find_element(By.XPATH, "//*[contains(text(), 'Sign In')]").click()
time.sleep(5)
username      = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
username.clear()
username.send_keys("joost@clickdrive.nl")
next = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='continueButton']").click()
time.sleep(5)
password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
password.clear()
password.send_keys("Seam123!")
next = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='continueButton']").click()
time.sleep(10)
start_shopping = driver.find_element(By.XPATH, "//*[contains(text(), 'Start Shopping')]").click()


#Importing websites
#df = pd.read_csv('')
#links = df['links']

links = ["https://www.faire.com/brand/b_39ejtly5?refC=All%20Products&refF=maker_value%3Amade_in_netherlands&sortingHint=true"]

for link in links:
    new_link = link + "&story=1" 
    driver.get(new_link)
    time.sleep(5)

    instagram_element = driver.find_element(By.CSS_SELECTOR, "a[target='_blank'][rel='noreferrer']").get_attribute('innerHTML')
    data = bs(instagram_element, 'html.parser')
    print(data.text)







