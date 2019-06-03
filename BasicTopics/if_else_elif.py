"""yas=int(input("Yasiniz?:"))

if yas >= 18:
	print("Mekana girebilirsiniz...")
else:
	print("Mekana giremezsiniz...")
"""


## 	Notlandirma##############################

"""
note = int(input("Notunuzu giriniz:"))

if note >= 90:
	print("AA aldiniz")
elif note >= 80:
	print("BA aldiniz")
elif note >= 70:
	print("BB aldiniz")
elif note >= 55:
	print("CB aldiniz")
elif note >= 45:
	print("CC aldiniz")
elif note == 13:
	print("Guzel not")
else:
	print("Kaldiniz")

"""


###	Kullanici ismi ve parola kontrolu

username=input("\nKullanici adinizi giriniz:")
password=input("\nParolanizi giriniz:")

if username == 'zumrud' and password == '1234':
	print('\nHosgeldiniz')
elif username == 'zumrud' and password !='1234':
	print('Hatali parola!')
elif username!='zumrud' and password == '1234':
	print('Boyle bir kullanici kayitli degil')
else:
	print('\nHatali giris')