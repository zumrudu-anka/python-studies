import requests
from bs4 import BeautifulSoup as bs

imdb_url = "https://www.imdb.com/chart/top"

r=requests.get(imdb_url)

soup = bs(r.content,"html.parser")

data=soup.find_all("table",{"class":"chart full-width"})    ## liste dondurur

movietable=(data[0].contents)[len(data[0].contents)-2]  ## tek elemanli listenin ilk elemaninin icerigi 7 elemanli. 5. indisteki eleman tbody

movietable=movietable.find_all("tr")

for movie in movietable:
    movie_title  = movie.find_all("td",{"class":"titleColumn"})
    movie_title = movie_title[0].text
    movie_title = movie_title.replace("\n","")
    print(movie_title)