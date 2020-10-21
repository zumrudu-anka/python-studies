# numbers = [1, 2, 3, 4, 5]

# iterator = iter(numbers)

# print(iterator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


########################################


class Remote():
    
    def __init__(self, remote_list):
        self.remote_list = remote_list
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.remote_list):
            return self.remote_list[self.index]
        else:
            self.index = -1
            raise StopIteration

kumanda = Remote(["Atv", "TRT", "Fox", "Show", "Star", "Kanal D"])

print(kumanda)

iterator = iter(kumanda)

print(iterator)

# next(iterator) # called next function and index is increased with it

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # Stop iteration


for i in kumanda: # we can use this, but now index is max length of the list
    print(i)

kumanda.index = -1

for i in kumanda:
    print(i)