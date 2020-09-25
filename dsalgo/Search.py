import sys

class Search:

	def __new__(self, array, algorithm, element):

		'''
		args:
	      :array: (list) : a python list
	      :algorithm: (str): Searching algorithm type
	                        Values supported are:
	                        1. linear
	                        2. binary

	      :element: Element whose index has to be found
	                if present  
	    
	    return:
	        Index of the element if found else returns -1
		'''


		self.array = array
		self.algorithm = algorithm
		self.element = element

		if self.algorithm == 'linear':
			return linear_search(self.array, self.element)

		elif self.algorithm == 'binary':
			return binary_search(self.array, 0, len(self.array)-1, self.element)

		else:
			stderr.write("Error: unsupported sorting algorithm passed!")


def linear_search(array, element):
	
	'''
	args:
      :array: (list) : a python list
      :element: Element whose index has to be found
                if present  
    
    return:
        Index of the element if found else returns -1
	'''

	for index, value in enumerate(array):
		if value == x:
			return index

	return -1



def binary_search(array, l, r, element): 
    '''
	args:
      :array: (list) : a python list
      :l(int): left index
      :r(int): right index
      :element: Element whose index has to be found
                if present  
    
    return:
        Index of the element if found else returns -1
	'''

    if r >= l: 
        mid = l + (r - l) // 2

        
        if array[mid] == element: 
            return mid 
        
        
        elif array[mid] > element: 
            return binary_search(array, l, mid-1, element) 


        else: 
            return binary_search(array, mid + 1, r, element) 

    else:  
        return -1

