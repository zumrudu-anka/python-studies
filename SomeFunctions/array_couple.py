import sys

def array_couple(arr):
	#this is not perfect
	"""odd_pairs = []
				if len(arr) > 1:
					found_on_last_pair=False
					for i in range (len(arr) - 2):
						founded = False
						#temp.append("{} {}".format(arr[i],arr[i+1]))
						for j in range(i + 2, len(arr)):
							if arr[j] == arr[i + 1] and arr[j+1] == arr[i]:
								founded=True
								if j ==len(arr)-2 or j == len(arr)-1:
									found_on_last_pair=True
						if not founded:
							odd_pairs.append("{} {}".format(arr[i],arr[i+1]))
					if not found_on_last_pair:
						odd_pairs.append("{} {}".format(arr[len(arr)-2],arr[len(arr)-1]))
					return odd_pairs
				else:
					return "".join(arr[0])"""
	#return odd_pairs

	temp=""
	for i in range(len(arr)):
		temp += arr[i] + " "
		if i%2 == 1:
			temp+=","
	temp = temp.split(" ,")
	store = []
	for i in temp:
		if i[::-1] not in temp:
			for j in i.split():
				store.append(j)
		elif i == i[::-1] and temp.count(i)<2:
			for j in i.split():
				store.append(j)
	if store == []:
		return "OK"
	return ",".join(store)

def main():
	print(array_couple(sys.argv[1:]))
	
if __name__ == "__main__":
	main()