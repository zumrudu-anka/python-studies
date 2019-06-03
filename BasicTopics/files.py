#dosya = open("C:/Users/pHoEniX/Desktop/dosya.txt","w")

#dosya = open("dosya.txt","w")
#dosya = open("dosya.txt","a")

#dosya.write("naber")


#dosya = open("dosya2.txt","r")  File not found

"""try:
	dosya=open("dosya2.txt","r")
except FileNotFoundError:
	print("Dosya Bulunamadi")"""

#dosya=open("dosya.txt","r")

#print(dosya.readline())
#print(dosya.readline())

"""liste=dosya.readlines()

for i in liste:
	print(i)

dosya.close()

"""

"""with open("dosya.txt","r") as dosya:
	dosya.seek(12)
	print(dosya.read(4))	#10. karakterden itibaren 5 karakter okur
	str1=dosya.read(10)
	print(str1)
	print(dosya.read(15))
	#dosya.seek(5)	## Burada yine dosyanin en basindan itibaren indexi 5 ilerletir
	#print(dosya.read())

with open("dosya2.txt","r+") as dosya2:
	veri=dosya2.read()
	dosya2.seek(0)
	veri="Yeni String" + veri
	dosya2.write(veri)"""

with open("dosya2.txt","r+") as dosya2:
	veri = dosya2.readlines()
	veri.insert(5,"En son falan")
	dosya2.seek(0)
	dosya2.writelines(veri)