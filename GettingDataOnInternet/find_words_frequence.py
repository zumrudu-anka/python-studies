import requests
from bs4 import BeautifulSoup as bs

url="https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"

allwords=[]

r=requests.get(url)

soup=bs(r.content,"html.parser")

for p in soup.find_all("p"):
    content = p.text
    words=content.lower().split()
    for word in words:
        allwords.append(word)
        print(word)