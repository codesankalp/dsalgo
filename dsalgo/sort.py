def sort(array,algo=None,reverse=False):
	if algo==None:
		return sorted(array,reverse=reverse)
	else:
		return exec(algo+'(reverse)')

def bubble(reverse=False):
	'''
	A bubble sort algorithm is an algorithm
	that repeatedly swaps adjacent elements.
	The smallest values comes in front and 
	large values goes at back, similar to that a
	lighter bubbles comes up, hence bubble sort
	'''
	n=len(array)
	for i in range(n):
		swap=0
		for j in range(0,n-i-1):
			if self.array[j]>self.array[j+1]:
				self.array[j],self.array[j+1]=self.array[j+1],self.array[j]
				swap=1
		if swap==0:
			break
	if reverse==True:
		return self.array[::-1]
	return self.array

if __name__ == '__main__':
	sort()
