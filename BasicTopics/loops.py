#############################			WHILE LOOPS		##########################


"""i=0

while(i<19):
	print('i\'nin degeri: {}'.format(i+1))
	i+=1"""


kullanici='zumrud'
sifre='1234'

while(True):
	username=input("\nKullanici adi:")
	password=input("\nParola:")
	if username != kullanici:
		print("\nBoyle bir kullanici kayitli degil")
	else:
		if password == sifre:
			print("\nHosgeldiniz!")
			break
		else:
			print("\nParolanizi yanlis girdiniz")
			print("\nSifrenizi degistirmek ister misiniz?(E/H)")
			cevap=input()
			if cevap == 'E':
				while(True):
					yenisifre=input("Yeni sifre:")
					yenisifre2=input("Yeni sifre tekrari:")
					if yenisifre == yenisifre2:
						print("Sifrenizi basariyla degistirdiniz")
						sifre=yenisifre
						break
					else:
						print("Hatali giris")


#############################			FOR LOOPS		##########################


"""string="ZumruduAnka"

liste = ['elma','armut','kiraz']

for i in string:
	print(i)

for i in liste:
	print(i)

for i in range(10):
	print(i*'*')

print(*range(2,10,3))

"""

###		FACT  	######

"""fact=1

while True:
	sayi=int(input("Faktoriyel almak icin sayi giriniz:"))
	if(sayi <= 0):
		print("Lutfen pozitif bir sayi giriniz:")
	else:
		for i in range(2,sayi+1):
			fact*=i
		print(fact)"""