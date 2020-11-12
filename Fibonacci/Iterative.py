def fib(n):
    
    if n == 0:
        return 0

    left = 0
    right = 1

    for i in range(1, n):
        left, right = right, left + right

    return right

print(fib(1))