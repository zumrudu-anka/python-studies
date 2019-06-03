## Matematiksel bir iki islem

print(4//3)	#Kalansiz bolme

print(4**3)	#Us alma islemi

## Tip donusumleri
print('zumrudu' + 'anka' + str(3) + str(4.5))

print(int('9')+5)

print(float('4.78')+56)

## Liste uzunlugu ve indisleri
a='anka'

print(a[1:3])

print(len(a))

print(a[:])

print(a[2:])

print(a[:4])

## Degisken tipleri
print(type(2.345))

print(type(('zumrudu','3')))

print(type(['zumrudu','3']))

print(type('zumrudu'))

print(type({'anka':'s'}))

## Bazi liste islemleri
oyuncu=['arda','turan',28,1.77]

oyuncu.append('barcelona')

print(oyuncu)

## Liste liste ile toplanir
oyuncu = oyuncu + ['atletico']

print(oyuncu)

print(oyuncu[0:3])

## Listenin ilgili indisleri asagidaki gibi guncellenebilir veya liste sifirlanabilir
oyuncu[:2]=['dani','alves']

print(oyuncu)

oyuncu[:2]=[]

print(oyuncu)

oyuncu[:]=[]

print(oyuncu)