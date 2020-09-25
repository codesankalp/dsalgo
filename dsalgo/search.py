import sys
import math

class Search:

    def __new__(self, array, element, algo):
        '''
        args:
            :array: (list) : a python list
            :algo: (str): searching algorithm type
                            values supported are:
                            1. Linear Search (linaer)
                            2. Binary Search (binary)
                            3. Jump Search (jump)
                            4. Fibonacci Search (fibonacci)
            :element -> element that want to be search
        return:
            index of search element
        '''
        self.array = array
        self.algo = algo
        self.element = element

        if self.algo == 'linear':
            return LinearSearch(self.array, self.element)
        elif self.algo == 'binary':
            return BinarySearch(self.array, self.element)
        elif self.algo == 'jump':
            return JumpSearch(self.array, self.element)
        elif self.algo == 'fibonacci':
            return FibonacciSearch(self.array, self.element)
        else:
            sys.stderr.write("Error: unsupported searchning algorithm passed!")


def LinearSearch(array, element):
    '''
    In linear search, a sequential search is made over all 
    items one by one. Every item is checked and if a match 
    is found then that particular item is returned, 
    otherwise the search continues till the end of the data collection.
    
    args:
        :array:(list) -> list to be sorted
        :element -> element that want to be search
    '''
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1


def BinarySearch(array, element):
    '''
    Binary search follows a divide and conquer methodology. 
    It is faster than linear search but requires that 
    the array be sorted before the algorithm is executed.
    
    If array is not sorted then it will give and worng answer to you.
    
    args:
        :array:(list) -> list to be sorted
        :element -> element that want to be search
    '''
    first = 0
    last = len(array) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last)//2
        if array[mid] == element:
            index = mid
        else:
            if element < array[mid]:
                last = mid -1
            else:
                first = mid + 1
    return index

        
def JumpSearch (array, element):
    '''
    Jump Search is similar to binary search.
    It works on sorted array and uses a similar
    divide and conquer approach to search through it.
    
    If array is not sorted then it will give and worng answer to you.
    
    args:
        :array:(list) -> list to be sorted
        :element -> element that want to be search
    '''
    
    length = len(array)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and array[left] <= element:
        right = min(length - 1, left + jump)
        if array[left] <= element and array[right] >= element:
            break
        left += jump
    if left >= length or array[left] > element:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and array[i] <= element:
        if array[i] == element:
            return i
        i += 1
    return -1
    
    
def FibonacciSearch(array, element):
    '''
    Fibonacci search is another divide and conquer algorithm 
    which bears similarities to both binary search and jump search. 
    It gets its name because it uses Fibonacci numbers to calculate 
    the block size or search range in each step.
    
    args:
        :array:(list) -> list to be sorted
        :element -> element that want to be search
    '''
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(array)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(array)-1))
        if (array[i] < element):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (array[i] > element):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(array)-1) and array[index+1] == element):
        return index+1
    return -1