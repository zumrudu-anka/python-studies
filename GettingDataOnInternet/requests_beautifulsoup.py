### Tum islemler python Shell uzerinde yapildi

import requests
from bs4 import BeautifulSoup

r=requests.get("https://yellowpages.com.tr/ara?q=Cafe")
r.content   ## Tum icerigi gosterir

soup=BeautifulSoup(r.content)
print(soup.prettify())

soup.find_all("a")

links=soup.find_all("a")

for link in links:
    print(link.get("href"))

for link in links:
    print(link.text)

for link in links:
    print(link.text,link.get("href"))