
# ? 1 #############################################

# class powersOfThree():
#     def __init__(self, max = 0):
#         self.max = max
#         self.power = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.power < self.max + 1:
#             result = 3 ** self.power
#             self.power += 1
#             return result
#         else:
#             self.power = 0
#             raise StopIteration

# power = powersOfThree(6)

# for i in power:
#     print(i)

# for i in power:
#     print(i)

# ? 2 #############################################

class squareOfNumbers():
    def __init__(self, max = 1):
        self.max = max
        self.power = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.power < self.max + 1:
            result = self.power ** 2
            self.power += 1
            return result
        else:
            self.power = 1
            raise StopIteration

iterator = iter(squareOfNumbers(5))

for i in iterator:
    print(i)