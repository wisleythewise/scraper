import requests 
from bs4 import BeautifulSoup as soup
import re
import time
import pandas as pd

websites = pd.read_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/orderchampwebsites.csv")


crm = []

for website in websites['websites']: 

    try: 
        print("this is the website: ", website)

        # add https
        url = "https://" + website
        
        source = requests.get(url)
        time.sleep(2)
        html = str(soup(source.content, 'html.parser'))
        if (re.findall(r'shopify', html)):
            crm.append("S")
        elif (re.findall(r'woocommerce', html)):
            crm.append("W")
        else:
            crm.append('U')
        print(crm)
    except: 
        print(crm)
        crm.append('website could not be loaded')

# export only the crm
crmSystem = {'crm' : crm}
backup = pd.DataFrame(crmSystem)
backup.to_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/orderchampMerchantCrm.csv")