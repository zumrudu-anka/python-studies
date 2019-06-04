import requests
from bs4 import BeautifulSoup as bs
import operator

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

def create_dictionary(all_words):
    word_count = {}
    for word in all_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


url="https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"

allwords=[]

r=requests.get(url)

soup=bs(r.content,"html.parser")

for p in soup.find_all("p"):
    content = p.text
    words=content.lower().split()
    for word in words:
        allwords.append(word)

allwords = clean_symbols(allwords)

word_count = create_dictionary(allwords)

for key,value in sorted(word_count.items(),key=operator.itemgetter(0)):
    print(key,value)