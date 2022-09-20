import pandas as pd 

df = pd.DataFrame()

websites = pd.read_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/orderchampSocials.csv")
handles=  pd.read_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/orderchampproductlinks.csv")
followers =  pd.read_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/orderchampwebsites.csv")
crm =  pd.read_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/orderchampMerchantCrm.csv")


frames = [websites, handles, followers,crm ]

result = pd.concat(frames, axis = 1)

result.to_csv("G:/My Drive/Werk/BV/SEAM/Scraper/scaper_data/format/orderchampMerged.csv")