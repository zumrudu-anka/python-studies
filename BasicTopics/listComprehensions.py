numbers = [x for x in range(10)]

numbers = [x**2 for x in range(10)]

numbers = [x * x for x in range(1,25) if x % 3 == 0]

numbers = [f"{x}: even" if x % 2 == 0 else f"{x}: odd" for x in range(15)]

numbers = [(x, y) for x in range(10) for y in range(10)]

numbers = [[x, y] for x in range(10) for y in range(10)]

numbers = [[x, y, z] for x in range(5) for y in range(4) for z in range (3)]

print(numbers)