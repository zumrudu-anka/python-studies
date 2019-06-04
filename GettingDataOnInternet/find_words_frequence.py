import requests
from bs4 import BeautifulSoup as bs

def clean_symbols(words):
    words_which_havent_symbols=[]
    symbols = "!@$#^*()_+{}\"<>?,.'/;[]-=`´" + chr(775)
    for word in words:
        for symbol in symbols:
            if symbol in word:
                word = word.replace(symbol,"")
        if len(word) > 0:
            words_which_havent_symbols.append(word)
    return words_which_havent_symbols

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

allwords = clean_symbols(allwords)

for word in allwords:
    print(word)