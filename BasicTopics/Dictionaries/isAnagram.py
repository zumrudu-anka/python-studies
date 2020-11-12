def isAnagram(word1, word2):
    if len(word1) != len(word2):
        return False
    
    word1_dict = {}
    word2_dict = {}

    for letter in word1:
        if letter not in word1_dict.keys():
            word1_dict[letter] = 1
        else:
            word1_dict[letter] += 1

    for letter in word2:
        if letter not in word2_dict.keys():
            word2_dict[letter] = 1
        else:
            word2_dict[letter] += 1

    return word1_dict == word2_dict

print(isAnagram("Ahmet", "tehmA"))