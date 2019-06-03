import math
import urllib.request
#import mutlak
#print(mutlak.mutlak(-5))

#from mutlak import *
#from mutlak import mutlak
#print(mutlak(-5))

urls={
	"url1" : "https://images.pexels.com/photos/67636/rose-blue-flower-rose-blooms-67636.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
	"url2" : "https://images.unsplash.com/photo-1500382017468-9049fed747ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
	"url3" : "https://images.pexels.com/photos/326055/pexels-photo-326055.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
}

url1 = "https://images.pexels.com/photos/67636/rose-blue-flower-rose-blooms-67636.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
url2 = "https://images.unsplash.com/photo-1500382017468-9049fed747ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80"
url3 = "https://images.pexels.com/photos/326055/pexels-photo-326055.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"

urllist=[url1,url2,url3]

"""say=1
for url in urllist:
	print(url)
	full_path= "images/" + "Resim" + str(say) + ".jpg"
	urllib.request.urlretrieve(url,full_path)
	say+=1
"""
image=urllib.request.urlopener()
image.retrieve("http://www.python.org/images/success/nasa.jpg","NASA.jpg")

"""
for url in urls.items():
	say=1
	print(url[1])
	urllib.request.urlretrieve("{}".format(url[1]),"Resim{}.jpg".format(say))
	say+=1"""

