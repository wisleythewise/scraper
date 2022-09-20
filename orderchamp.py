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
import numpy as np

# Get that session
# Go given page
driver = webdriver.Chrome('G:\My Drive\Werk\BV\SEAM\Scraper\chomium\chromedriver_win32\chromedriver.exe')

driver.get("https://www.orderchamp.com/#")
time.sleep(5)

# Go to logging in page
sideMenu = driver.find_element(By.XPATH, "//*[contains(text(), '    Log in')]").click()

time.sleep(5)
username      = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
username.clear()
password.clear()
username.send_keys("joost@clickdrive.nl")
password.send_keys("Seam123!")
time.sleep(5)
next = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)

#Importing websites

websites =  pd.read_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/orderchampproductlinks.csv")


brand = []

for website in websites["link-href"]:
    
    # Generate placeholders    
    placeholder = ["x","x","x","x","x"]

    try:
        time.sleep(5)
        driver.get(website)
        time.sleep(5)

        # Get titles 
        title = driver.find_element(By.CSS_SELECTOR, "h1[class='heading-4 lg:heading-3 mb-6']").text
        placeholder[0] = title
        # Get socials

        socials = driver.find_elements(By.CSS_SELECTOR, "a[target='_blank'][class='btn-tiny btn btn-white']")

        switch = 0
        for social in socials:

            print("check")
            html = str(bs(social.get_attribute("innerHTML"), 'html.parser'))                   
            if re.search("instagram", html, re.IGNORECASE):
                print("instgram")
                placeholder[1] = social.get_attribute("href")
                if (social.text != []):
                    placeholder[2] = social.text 
                else:
                    placeholder[2] = "X" 
            
            if re.search("facebook", html, re.IGNORECASE):

                print("Facebook")

                placeholder[3] = social.get_attribute("href")
                
                if (social.text != []):
                    placeholder[4] = social.text 
                else:
                    placeholder[4] = "X" 
            
        brand.append(placeholder)
    except: 
        print("something went wrong")
        time.sleep(5)
        brand.append(placeholder)


    print(brand)            


# export only the handles

df = pd.DataFrame()

brand = np.array(brand)

df["brandName"] = brand[:,0]
df["instagramLinks"]  = brand[:,1]
df["instagramFollowers"] = brand[:,2]

df["facebookLinks"] = brand[:,3]
df["facebookFollowers"] = brand[:,4]


df.to_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/orderchampSocials.csv")
