
# ? Generatorler bellekte yer kaplamıyor ?

################################

# def printSquareOfNumbers():

#     result = []

#     for i in range(1, 6):
#         result.append(i ** 2) 
#       # ! bu dongude degerleri uretmis ve listeye atmis oluyoruz
#       # ! 100000 deger yazdiracak olsak bellekte bayagi yer kaplayacak
#     return result

# print(printSquareOfNumbers())


#################################

# ? With Generators

# def printSquareOfNumbers():
#     for i in range(1, 6):
#         yield i ** 2
#         # ! yield anahtar kelimesi ile aslinda burada bu degerler henuz
#         # ! uretilmemis durumda. O yuzden su anda generator nesnesi bos

# generator = printSquareOfNumbers()

# print(generator)

# iterator = iter(generator) 
# # ? Generatorler iterable nesnelerdir ve iterator araciligi ile
# # ? gerekli elemanlari yield anahtar sozcugu bize saglar.
# # ? Biz next iteratoru cagirmadigimiz surece yield anahtar sozcugu deger uretmez
# # ? yani generator orada takilir biz next iteratoru isteyene kadar.j
# # ? dondurulen nesne donduruldukten sonra tarihe karisir eger bir degiskende saklamazsak                        

# print(next(iterator)) # ? burada yazdirilan 1 yazdirildiktan sonra tarihe karisiyor.
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # ? su anda son indexe geldik. Bu generatorun artik isi bitti.
# # ? yeniden generator olusturabilirim. Fakat ayni generator ile tekrar
# # ? iterator olusturursak hata aliriz

# iterator2 = iter(generator)

# print(next(iterator2))

##############################################

# ! Generators with List Comprehension

# numbers = [i * 3 for i in range(5)]

# print(numbers)

# generator = (i * 3 for i in range(5)) # ? this will be created generator object

# print(generator)

# iterator = iter(generator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


########################################

# ? Example

def multiplicationTable():
    for i in range(1, 11):
        for j in range(1, 11):
            yield f"{i} x {j} = {i * j}"

for i in multiplicationTable():
    print(i)