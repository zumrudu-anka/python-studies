def findRepeatingLetters(word):
    word_dict = {}

    repeatedLetters = []

    for letter in word:
        if letter not in word_dict:
            word_dict[letter] = 1
        else:
            word_dict[letter] += 1
    
    for key, value in word_dict.items():
        if value > 1:
            repeatedLetters.append(key)
    
    return repeatedLetters

print(findRepeatingLetters("abc"))