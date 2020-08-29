import sys

class Sort:
    # def __init__(self, array, algo, reverse=False):
    #     '''
    #     args:
    #       :array: (list) : a python list
    #       :algo: (str): sorting algorithm type
    #                         values supported are:
    #                         1. bubble
    #       :reverse: (bool) : default = False
    #                         if True order is reversed.
    #     return:
    #         sorted array
    #     '''
    #     self.array = array
    #     self.algo = algo
    #     self.reverse = reverse

    def __new__(self, array, algo, reverse=False):
        '''
        args:
          :array: (list) : a python list
          :algo: (str): sorting algorithm type
                            values supported are:
                            1. bubble
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
