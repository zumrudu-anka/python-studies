# def wordPermutation(word, left = ""):
#     if len(word) == 0:
#         print(left)
    
#     else:
#         for i in range(len(word)):
#             wordPermutation(word[:i] + word[i + 1:], left + word[i])




############# Best Solution ##############

def wordPermutation(word):
    if len(word) == 1:
        return word

    result = []
    for i in range(len(word)):
        character = word[i]
        diff = word[:i] + word[i + 1:]

        diffPermutations = wordPermutation(diff)

        for permutation in diffPermutations:
            result.append(character + permutation)
    
    return result

print(wordPermutation("abcd"))

