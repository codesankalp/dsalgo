# Returns index of x in the list/array if present, else -1 
def Linear_Search(arr, x):
	for index, element in enumerate(arr):
		if element == x:
			return index

	return -1


if __name__ == '__main__': 
    arr = [2, 4, 6, 8, 10] 
    x = 10

    result = Linear_Search(arr, x) 

    if result != -1: 
        print ("Element is present at index ", result) 
    else: 
        print ("Element is not present in the array") 
