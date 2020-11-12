############### Bad Way  ###############

# def f(n):
    
#     if n < 1:
#         return 0

#     elif n == 1 or n == 2:
#         return n
    
#     elif n == 3:
#         return 4

#     else:
#         return f(n - 1) + f(n - 2) + f(n - 3)


################### Good Way ##############

memo = {}

def f(n):
    
    if n < 1:
        return 0

    elif n == 1 or n == 2:
        return n
    
    elif n == 3:
        return 4

    if n not in memo.keys():
        memo[n] = f(n - 1) + f(n - 2) + f(n - 3)
    
    return memo[n]

print(f(4))