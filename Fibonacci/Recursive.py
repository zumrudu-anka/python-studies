# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     return fib(n - 1) + fib(n - 2)

# print(fib(2))

## Kotu cozum. Cunku olusan agacta fib degerleri sol ve sag
## dallanmalarda da hesaplaniyor.
## fib(3) + fib(2) icin => agacta fib(1), fib(2) iki kere hesaplaniyor



################# Daha iyi yol #################

memo = {}

def fib(n):
    if n == 0 or n == 1:
        return n

    if n not in memo.keys():
        memo[n] = fib(n - 1) + fib(n - 2)
    
    return memo[n]

print(fib(50))