import requests
from bs4 import BeautifulSoup
#import pandas as pd

URL = "http://www.op.gg/champion/garen/statistics/top/item"

opgg = requests.get(URL)
html = opgg.text
soup = BeautifulSoup(html, 'html.parser')
item_box = soup.find("div", class_="l-champion-statistics-content__side")
item_list = item_box.findAll("span",)

a=0

for i in item_list:
    print(str(a)+"위:"+i.string)
    a=a+1
