def mostRepeatedLetter(word):
    word_dict = {}
    maximumCount = 0
    result = ""

    for letter in word:
        if letter not in word_dict.keys():
            word_dict[letter] = 1
        else:
            word_dict[letter] += 1

    for key, value in word_dict.items():
        if value >maximumCount:
            result = key
            maximumCount = value
    return result

print(mostRepeatedLetter("Merhaba"))