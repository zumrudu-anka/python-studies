import sys


def rotate_array(arr):
	return "".join(i for i in arr[int(arr[0]):] + arr[:int(arr[0])])


def main():
	print(rotate_array(sys.argv[1:]))

if __name__ == "__main__":
	main()