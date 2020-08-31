import sys

class Sort:

    def __new__(self, array, algo, reverse=False):
        '''
        args:
          :array: (list) : a python list
          :algo: (str): sorting algorithm type
                            values supported are:
                            1.bubble
                            2.merge
                            3.bubble_recursion
                            4.selection
                            5.quick

          :reverse: (bool) : default = False
                            if True order is reversed.
        return:
            sorted array
        '''
        self.array = array
        self.algo = algo
        self.reverse = reverse

        if self.algo == 'bubble':
            return bubble(self.array, self.reverse)
        if self.algo == 'merge':
            return merge(self.array, self.reverse)
        if self.algo =='bubble_recursion':
            return bubble_recursion(self.array,self.reverse)
        if self.algo =='selection':
            return selection(self.array,self.reverse)
        if self.algo =='quick':
            return quick(self.array,self.reverse)
        else:
            sys.stderr.write("Error: unsupported sorting algorithm passed!")
        
def bubble(array, reverse=False):
    '''
    A bubble sort algorithm is an algorithm
    that repeatedly swaps adjacent elements.
    The smallest values comes in front and 
    large values goes at back, similar to that a
    lighter bubbles comes up, hence bubble sort

    args:
      :array:(list) -> list to be sorted
      :reverse:(boolean) -> default = False,
                            can be True for sort 
                            in reverse order
    '''
    n=len(array)
    for i in range(n):
        swap=0
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                swap=1
        if swap==0:
            break
    if reverse==True:
        return array[::-1]
    return array

def merge(array,reverse=False):


    """1.Divide:
    If q is the half-way point between p and r, then we can split the subarray A[p..r] 
    into two arrays A[p..q] and A[q+1, r].
    2.Conquer:
    In the conquer step, we try to sort both the subarrays A[p..q] and A[q+1, r]. 
     If we haven't yet reached the base case,
     we again divide both these subarrays and try to sort them.
    3.Combine:
    When the conquer step reaches the base step and we get two sorted subarrays A[p..q] and A[q+1, r] for array A[p..r],
    we combine the results by creating a sorted array A[p..r] from two sorted subarrays A[p..q] and A[q+1, r].
    """
    
    if len(array) >1: 
        mid = len(array)//2  # mid
        left = array[:mid]   # Dividing the array elements  
        right = array[mid:]  # into 2 halves 
  
        merge(left)        # Sorting the first half 
        merge(right)       # Sorting the second half 
        i = j = k = 0
          
        # Copy data to left[] and right[] 
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                array[k] = left[i] 
                i+= 1
            else: 
                array[k] = right[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(left): 
            array[k] = left[i] 
            i+= 1
            k+= 1
          
        while j < len(right): 
            array[k] = right[j] 
            j+= 1
            k+= 1
    if reverse==True :
     return array[::-1]
    return array

def bubble_recursion(array,reverse=False): 
    for i, num in enumerate(array): 
        try: 
            if array[i+1] < num: 
                array[i] = array[i+1] 
                array[i+1] = num 
                bubble_recursion(array) 
        except IndexError: 
            pass
    if reverse==True:
     return array[::-1]
    return array

def selection(array,reverse=False):
    """The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
       from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

        1) The subarray which is already sorted.
        2) Remaining subarray which is unsorted.
        In every iteration of selection sort, the minimum element (considering ascending order)
        from the unsorted subarray is picked and moved to the sorted subarray."""

    for i in range(len(array)): 
         min_idx = i 
         for j in range(i+1, len(array)): 
             if array[min_idx] > array[j]: 
                 min_idx = j
         array[i], array[min_idx] = array[min_idx], array[i] #Swapping values

    if reverse==True:
     return array[::-1]

    return array  

def quick(array,reverse=False):
    """The algorithm can be broken down into three parts​​:
       1.Partitioning the array about the pivot.
       2.Passing the smaller arrays to the recursive calls.
       3.Joining the sorted arrays that are returned from the recursive call and the pivot.
       
    """
    start=0
    end=len(array)-1
    quick_sort(array,start,end)

    if reverse==True:
      return array[::-1]

    return array

def quick_sort(array, start, end):
      if start >= end:
         return

      p = partition(array, start, end)
      quick_sort(array, start, p-1)
      quick_sort(array, p+1, end)

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        #If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

