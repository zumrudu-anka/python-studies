import random
import itertools
import statistics

grades = random.choices(range(0, 101), k = 60)
print(grades)

for grade in grades:
    print(grade)

for grade in grades:
    print(grade - statistics.mean(grades))

deviation = []

for grade in grades:
    deviation.append(grade - statistics.mean(grades))


new_list = list(itertools.repeat(0, 60)) # 0 elemanlarından oluşan 60 elemanlı bir liste oluşturur

print(new_list)

for i in range(0, 60):
    new_list[i] = grades[i] - statistics.mean(grades)
    print("tur sayisi: " + str(i + 1))

print(new_list)