import random

print(random.randrange(0, 10)) # Belirli bir araliktan rastgele sayi uretme
print(random.sample(range(0, 10), 8)) # Belirlenen aralikta belirlenen k sayisi kadar eşsiz değerden oluşan liste üretme
print(random.choices(range(0, 10), k = 20)) # Belirlenen araliktan belirlenen k sayisi uzunlugunda rastgele degerlerden olusan bir liste uretme
print(random.randrange(2, 20, 2)) # randrange fonksiyonunun 3. parametresi rastgele üretilecek sayının adım miktarını belirtir.
# Yani ilk parametreden itibaren bu adım kadar sayarak rastgele bir deger üretir
print(random.randrange(100, 1000, 25))
print(random.randrange(-50, -5))
print(random.randrange(-50, -5, 5))

print(random.randint(0, 100))