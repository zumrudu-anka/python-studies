import sys

def character_freq_in_string(word):
    controlled_characters = []
    
    #First Method
    
    """
    for i in range(len(word)):
        count = 1
        if word[i] not in controlled_characters:
            for j in range(i+1,len(word)):
                if word[i] == word[j]:
                    count += 1
            controlled_characters.append(count)
            controlled_characters.append(word[i])

    return "".join(str(i) for i in controlled_characters)
    """
    
    #Other Method
    for i in word:
        if i not in controlled_characters:
            controlled_characters.append(word.count(i))
            controlled_characters.append(i)
    return "".join(str(i) for i in controlled_characters)

    #One More
    """
    i=0
    while i < len(string):
        
        l = string[i]
        liste = [0,l]
        
        for j in range(len(string)):
            if string[j] == l:
                liste[0] += 1   
 
        freq_str += "".join(map(str,liste))
        string = string.replace(l, "")    
    return freq_str
    """
def main():
    for arg in sys.argv[1:]:
        print(character_freq_in_string(arg))

if __name__ == "__main__":
    main()