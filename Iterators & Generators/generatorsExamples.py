
# ? 1 #############################################

# def fibonacci():
#     a = b = 1
#     yield a
#     yield b

#     while True:
#         a, b = b, a + b
#         yield b

# for num in fibonacci():
#     print(f"{num}")
#     if num > 50000:
#         break

# ? 2 #############################################

def isPrime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i < number / 2 + 1:
        if number % i == 0:
            return False
        i += 2
    return True

def getPrime():
    i = 2
    while True:
        if (isPrime(i)):
            yield i
        i += 1

for number in getPrime():
    if number > 1000:
        break
    print(number)