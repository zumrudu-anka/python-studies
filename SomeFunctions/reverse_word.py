import sys

def reverse_word(word):
	"""
	drow=""
	for i in reversed(word):
		drow += i
	print(word)
	return drow
	"""

	#Other Method
	"""
	drow=""
	for i in range(len(word)-1,-1,-1):
		drow += word[i]
	print(word)
	return drow
	"""

	#One More
	print(word)
	return word[::-1]

def main():
	for arg in sys.argv[1:]:
		print(reverse_word(arg))

if __name__ == "__main__":
	main()