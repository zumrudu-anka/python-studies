"""a=input("birinci sayi")
b=input("ikinci sayi")
c=input("ucuncu sayi")

print('sayilarin toplami:', int(a)+int(b)+int(c))

	"""
print('Oyuncu Kaydetme Programi')

ad=input('\nOyuncu adi:')
soyad=input('\nOyuncu soyadi:')
takim=input('\nOyuncu takimi:')
bilgiler=[ad,soyad,takim]

print("\nVeritabanina kaydediliyor...")

#print("\nOyuncunun adi:",ad,"\nOyuncunun soyadi:",soyad,"\nOyuncunun takimi:",takim)

print("\nKaydedildi...")

print("\nOyuncunun adi: {} \nOyuncunun soyadi: {} \nOyuncunun takimi: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))