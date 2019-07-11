import sys

def find_lost_digit(equation):
	index = equation.index("=")
	for i in range(10):
		temp_equation = equation.replace("x",str(i))
		if eval(temp_equation[:index]) == eval(temp_equation[index+1:]):
			return i

def main():
	equation=""
	count = 0
	for arg in sys.argv[1:]:
		if count == 0:
			equation += arg
		else:
			equation += " " + arg
	print(find_lost_digit(equation))

if __name__ == "__main__":
	main()