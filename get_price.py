import requests
from bs4 import BeautifulSoup
#import pandas as pd

URL = "https://finance.naver.com/item/main.nhn?code=005930"

samsung_electronic = requests.get(URL)
html = samsung_electronic.text

soup = BeautifulSoup(html, 'html.parser')

finance_html = soup.findAll("div", class_="sub_section")
result = finance_html[4].find("tbody", class_="")
result2 = result.findAll("td", class_="" )
result3 = result.findAll("th",)


def PLheader():
    a = 0
    for spacedel in result3:
        spacedel = spacedel.string
        result3[a]=spacedel
        a=a+1
    return


def PLdata(): 
    a = -1
    for spacedel in result2:
        a=a+1
        #if( (spacedel.string is None) or (len(spacedel.string) == 0)):
        #    continue
        spacedel = spacedel.string
        spacedel = ''.join(spacedel.split())
        result2[a]=spacedel
    return

def runrunrun():
    a=[]
    for aa in range(0,14):
        a.append(result2[aa*10:aa*10+9])
    return a



    
#s=pd.Series(a)  
#print(s)


