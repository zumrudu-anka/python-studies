################## 		FACTORIAL  	#########################

"""def factorial(numara):
	result=1
	for i in range(2,numara+1):
		result*=i
	print("\n{}".format(result))

while True:
	print("\n Sonlandirmak icin 0 giriniz")
	sayi=int(input("\nFaktoriyel hesabi icin sayi giriniz: "))
	if(sayi == 0):
		print("\nProgram sonlandi")
		break
	else:
		factorial(sayi)"""


################## 		2. DERECE DENKLEMIN KOKBUL  	#########################

"""
def kokbul(a,b,c):
	delta=(b*b - 4*a*c)
	if delta < 0:
		print("Reel Kok Bulunamadi")
		return
	else:
		x1=(-b - delta**0.5)/2*a
		x2=(-b + delta**0.5)/2*a
	return (x1,x2)

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

sonuc=kokbul(a,b,c)

print(sonuc)


"""


####################		DEFAULT PARAMETRE		#######################

"""def kayit_ekle(ad="bilgi yok",soyad="bilgi yok",yas="bilgi yok",meslek="bilgi yok"):
	print("Kayit ekleniyor...")
	print("Ad: {}\nSoyad: {}\nYas: {}\nMeslek: {}\n".format(ad,soyad,yas,meslek))
	print("Kayit eklendi...")

ad=input("Ad: ")
soyad=input("Soyad: ")
yas=input("Yas: ")
meslek=input("Meslek: ")

#kayit_ekle(ad,soyad)	## Bu sekilde default parametreler sirayla ataniyor. Python anlamiyor
kayit_ekle(ad=ad,soyad=soyad,yas=yas,meslek=meslek)

"""

#### 			SEKiLLER		######
"""
			def geometri(sekil):
				if len(sekil) == 3:
					a=sekil[0]
					b=sekil[1]
					c=sekil[2]
					if (a + b) > c and (a+c) > b and (b+c) > a:
						if a == b and b == c:
							print("Eskenar Ucgen")
						elif a == b or a==c or b==c:
							print("ikizkenar Ucgen")
						else:
							print("Cesitkenar Ucgen")
					else:
						print("Ucgen belirtmiyor")
				elif len(sekil) == 4:
					a=sekil[0]
					b=sekil[1]
					c=sekil[2]
					d=sekil[3]
					if a == b and b == c and c == d:
						print("Kare")
					elif a == c and b == d:
						print("Dikdortgen")
					else:
						print("Dortgen")
			
			while True:
				kenar = int(input("\nLutfen Kenar Sayisi Giriniz(Cikmak icin 0): "))
				if kenar == 3:
					a=int(input("\na: "))
					b=int(input("\nb: "))
					c=int(input("\nc: "))
					geometri([a,b,c])
				elif kenar == 4:
					a=int(input("\na: "))
					b=int(input("\nb: "))
					c=int(input("\nc: "))
					d=int(input("\nd: "))
					geometri([a,b,c,d])
				elif kenar == 0:
					break
				else:
					print("Lutfen tekrar giriniz..")
"""			

############### 		RECURSION		####################


def topla(liste):
	toplam=0
	for i in liste:
		toplam+=i
	return toplam

print(topla([1,2,3,4]))

def topla2(sayi):
	if sayi == 1:
		return sayi
	#sayi += topla2(sayi-1)
	#return sayi
	return sayi + topla2(sayi-1)

def topla3(liste):
	if len(liste) == 1:
		return liste[0]
	return liste[0] + topla3(liste[1:])

print(topla2(4))
print(topla3([1,2,3,4]))