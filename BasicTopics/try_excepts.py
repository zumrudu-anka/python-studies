"""sayi1=input("\nSayi1: ")
sayi2=input("\nSayi2: ")

try:
	sayi1=int(sayi1)
	sayi2=int(sayi2)
	print(sayi1/sayi2)

except (ValueError,ZeroDivisionError):
	print("Bir Hata olustu...")

except ValueError:
	print("Lutfen 10'luk tabanda bir sayi giriniz...")

except ZeroDivisionError:
	print("Bir sayi sifira bolunemez...")
"""

try:
	dosya = open("dosya.txt","r")
except IOError:
	print("Dosya Bulunamadi.")
finally:
	dosya.close()