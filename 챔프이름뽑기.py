import requests
from bs4 import BeautifulSoup
#import pandas as pd

URL = "http://www.op.gg/champion/statistics"
cookies={'customLocale':'ko_KR'}
opgg = requests.get(URL, cookies=cookies)
html = opgg.text
soup = BeautifulSoup(html, 'html.parser')
#item_box = soup.findAll("a", class_="champion-index__champion-item__name")
item_box = soup.find("div", class_="champion-index__champion-list" )

champ_list=[]
for abce in item_box:
    champ_list.append([abce.get('data-champion-name'),abce.get('data-champion-key')])

print(champ_list)

#item_list = item_box.findAll("span",)  


