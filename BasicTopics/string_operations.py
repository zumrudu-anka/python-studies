country = "türkiye Cumhuriyeti"
print(country.capitalize()) # ilk harf buyuk
print(country.casefold()) # Butun harfler kucuk
print(country.center(40, "-")) # ifade 40 karakterden kucukse 40 karaktere sigacak sekilde buyutur ve ortalar. sag ve soldaki bosluklari 2. parametre ile doldurur

sentence = """
    Python derslerine başladım
    Python aslında öğrenmesi çok kolay bir dil
    Python öğrenmesi çok keyifli
"""
print(sentence)
print(sentence.count("Python"))
print(sentence.endswith("."))
print(sentence.find("dil"))

bread = "Ekmek sadece {price:.2f} Türk lirası!"
print(bread.format(price = 4.5))

name = "Benim adım {person_name} ve {person_age} yaşındayım".format(person_name = "Osman", person_age = 30)
print(name)

place = "Benim doğum yerim {0}, doğum yılım ise {1}".format("Erzurum", 1990)
print(place)

heat = "Saat {} ve hava {} santigrat derece.".format("23:15", 23)
print(heat)

print(sentence.index("derslerine")) # belirtilen ifadenin degiskende ilk gectigi yerin indeksini dondurur

print("Bu metnin tamamı rakamlardan olusuyor".isalnum())
print("23454".isalnum())

print("Bumetnin tamamı karakterlerden olusur".isalpha()) # Metinde sadece alfabetik karakterler mi var
print("Bumetnintamamıkarakterlerdenolusur".isalpha())

stationary = (
    "kalem",
    "kağıt",
    "defter",
    "silgi"
)
print(stationary)
print(" & ".join(stationary))

print(country.lower())
print(country.upper())

car = "       Otomobil        "
print(car)
print(car.lstrip())

wrong_sentence = """
    Aslında men mu yazıyı yazarken yanlışlık oldu.
    Nedense mir kere de değil
"""
print(wrong_sentence)
translation_table = wrong_sentence.maketrans("m", "b")
true_sentence = wrong_sentence.translate(translation_table)
print(true_sentence)

sentence_partition = "Elma çok lezzetli"
print(sentence_partition.partition("Elma")) # metni verilen ayırıcıya gore 3 parcaya boler
print(sentence_partition.partition("çok"))

sentence2 = "Erzurum Türkiye'nin başkentidir."
print(sentence2.replace("Erzurum", "Ankara"))

sentence3 = "Su sıcaktı. Su içmek istedim. Su içemedim"
print(sentence3.rfind("Su"))
print(sentence3.rindex("Su"))

line_partition = """
    Birinci satır
    İkinci satır
    Üçüncü satır
"""
print(line_partition)
print(line_partition.splitlines())

change_letter = "mERHABA bEN eRZURUM'DA dOĞDUM"
print(change_letter.swapcase())

title = "python derslerine giriş - 1"
print(title.title())

fill = "50"
print(fill.zfill(10)) # numerik bir stringi verilen parametre kadar genisleterek solunu 0'la doldurur

print(dir(sentence))