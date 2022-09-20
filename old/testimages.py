import requests
from bs4 import BeautifulSoup as soup
from PIL import Image

website = requests.get("https://bazou.nl/shop/armbanden/colorful-bracelets/gouddraad-armbandje-met-hartje-mint-roze/")

html = soup(website.content, "html.parser")

images = html.find_all("img")

print(images[0]['src'])

pic = Image.open(requests.get(images[0]['src'], stream = True ).raw)

print(pic.size)