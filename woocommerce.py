import requests 
from bs4 import BeautifulSoup as soup
import re
import feedparser
import pandas as pd
from PIL import Image

import requests
from bs4 import BeautifulSoup as soup
from PIL import Image


#websites = pd.read_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/faireMerchantWebsites.csv")

websites = ["bazou.nl/feed/?post_type=product"]

Title = []
Link = []
Photo = []


for website in websites:
    
    # get url
    url = "https://" + website
    NewsFeed = feedparser.parse(url)
    entries = NewsFeed.entries


    # loop over entries 
    for entry in entries:
        
        # Title product
        try:
            Title.append(entry['title'])
        except:
            Title.append("No title found")
            print("No title found")

        # Links
        try: 
            Link.append(entry['links'][0]['href'])

            # Photos
            try: 
                website = requests.get("https://bazou.nl/shop/armbanden/colorful-bracelets/gouddraad-armbandje-met-hartje-mint-roze/")
                html = soup(website.content, "html.parser")
                images = html.find_all("img")

                # Get Image
                try: 
                    #Get biggest image
                    bigImageSize = 0
                    for image in images:
                                pic = Image.open(requests.get(images[0]['src'], stream = True ).raw)
                                if (pic.size[0] > bigImageSize):
                                    bigImageSize = pic.size[1]
                                    print(bigImageSize)
                                    
                    Photo.append(images[0]['src'])
                except: 
                    Photo.append("No image found")
                    print("No image found")

            except: 
                print("Link request failed")

        except: 
            Link.append("No link was found")
            print("No link was found")


    #
    print(Photo) 
