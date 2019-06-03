"""sozluk = {
	"python":"Guzel bir dil",
	"PHP":"Script Dili",
	"Java":"Compile edilen dil"
}

print(sozluk["python"])

for i in sozluk.items():
	print("\n {}".format(i))
	print("\n {}".format(i[0]))
	print("\n" + i[0] + " " + i[1])


for i,j in sozluk.items():
	print("\n" + i+" "+j)"""


dersler={
	"Ahmet":["Veritabani","isletim sistemleri"],
	"Oguz":["Java","OOP"],
	"Mehmet":["Lineer Cebir","Diferansiyel Denklemler"]
}

isim=input("\nİsim Giriniz:")

print(dersler["{}".format(isim)])

for i in dersler.items():
	if i[0] == isim:
		for j in i:
			print(j)

for i in dersler[isim]:
	print(i)