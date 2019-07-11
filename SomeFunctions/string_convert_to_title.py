import sys

def frst_char_convert_to_uppercase(count,word):
	result=""
	word = word.lower()
	if count == 0:
		result += word[0].upper()
		for i in range(1,len(word)):
			result += word[i]
		return result
	else:
		return " " + word


def main():
	result=""
	count=0
	for arg in sys.argv[1:]:
		
		result += frst_char_convert_to_uppercase(count,arg)
		count += 1
	print(result)
if __name__ == "__main__":
	main()