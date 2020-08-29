class Sort:
    def __init__(self, array):
        self.array = array
        
    def bubble(self, reverse=False):
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
        n=len(self.array)
        for i in range(n):
            swap=0
            for j in range(0,n-i-1):
                if self.array[j]>self.array[j+1]:
                    self.array[j],self.array[j+1]=self.array[j+1],self.array[j]
                    swap=1
            if swap==0:
                break
        if reverse==True:
            return array[::-1]
        return self.array
