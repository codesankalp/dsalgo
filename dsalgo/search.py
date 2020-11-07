import math


class Search:

    def __init__(self, arr, number):
        """
            Class to search a number in array

            :args:    arr (list) -> number to search from
                      n (int)    -> number to search

            :return:  index (int) -> if number found
                     -1 (int)     -> if not found
        """
        self.arr = arr
        self.number = number

    def binary_search(self):

        """
            Binary Search:
                Search a sorted array by repeatedly
                dividing the search interval in half.
                Begin with an interval covering the whole array.
                If the value of the search key is less than
                the item in the middle of the interval,
                narrow the interval to the lower half.
                Otherwise narrow it to the upper half.
                Repeatedly check until the value is found or the
                interval is empty.

            params : array/list arr, x --> search value

            return : found --> returns index, not found --> -1
        """
        arr = sorted(self.arr)
        x = self.number
        low = 0
        high = len(arr) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2
            if arr[mid] < x:
                low = mid + 1

            elif arr[mid] > x:
                high = mid - 1

            else:
                return mid

        return -1

    def linear_search(self):
        """
            Linear Search
                Start from the leftmost element of arr[] and one by
                one compare x with each element of arr[]
                If x matches with an element, return the index.
                If x doesn’t match with any of elements, return -1.

            params : array/list --> arr, value --> x

            return : found --> int index, not found --> -1

        """
        arr = self.arr
        x = self.number
        for i in range(len(arr)):

            if arr[i] == x:
                return i

        return -1

    def jump_search(self):
        """
            Jump Search

                Like Binary Search, Jump Search is a searching algorithm for
                sorted arrays. The basic idea is to check fewer elements
                (than linear search) by jumping ahead by fixed steps
                or skipping some elements
                in place of searching all elements.

            params : array --> arr, value --> x

            returns : found --> int index, not found --> -1

        """
        arr = sorted(self.arr)
        x = self.number
        flag = 0
        interval = int(math.sqrt(len(arr)))
        for i in range(0, len(arr), interval):
            if arr[i] > x:
                chunk = i
                flag = 1
                break
            if arr[i] == x:
                return i
        if flag == 0:
            c = i
            for j in arr[i:]:
                if j == x:
                    return c
                c += 1
        else:
            arr_ls = arr[chunk-interval:chunk]
            ind = [i for i, d in enumerate(arr_ls) if d == x]
            return chunk-interval+ind[0]

    def interpolation_search(self):

        """
            Interpolation Search
                The Interpolation Search is an improvement over Binary Search
                for instances, where the values in a sorted array are uniformly
                distributed. Binary Search always goes to the middle element
                to check. On the other hand, interpolation search may go to
                different locations according to the value of the key being
                searched.

            params : array --> arr, array length --> length, value --> x

            return : found --> int index, not found --> -1
        """
        arr = sorted(self.arr)
        x = self.number
        length = len(arr)
        lo = 0
        hi = (length - 1)

        while lo <= hi and x >= arr[lo] and x <= arr[hi]:
            if lo == hi:
                if arr[lo] == x:
                    return lo
                return -1

            pos = lo + int(((float(hi - lo) /
                             (arr[hi] - arr[lo])) * (x - arr[lo])))

            if arr[pos] == x:
                return pos

            if arr[pos] < x:
                lo = pos + 1

            else:
                hi = pos - 1
        return -1

    def fibonacci_search(self):

        """
            Fibonacci Search
                The idea is to first find the smallest Fibonacci number
                that is greater than or equal to the length of given array.
                Let the found Fibonacci number be fib (m’th Fibonacci number).
                We use (m-2)’th Fibonacci number as the index
                (If it is a valid index). Let (m-2)’th Fibonacci Number be i,
                we compare arr[i] with x, if x is same, we return i.
                Else if x is greater, we recur for subarray after i,
                else we recur for subarray before i.

            Params : array --> arr, value --> x, array length

            return : found --> int index, not found --> -1

        """
        arr = sorted(self.arr)
        x = self.number
        arr_len = len(arr)
        fibMMm2 = 0    # (m-2)'th Fibonacci No.
        fibMMm1 = 1    # (m-1)'th Fibonacci No.
        fibM = fibMMm2 + fibMMm1   # m'th Fibonacci

        while (fibM < arr_len):
            fibMMm2 = fibMMm1
            fibMMm1 = fibM
            fibM = fibMMm2 + fibMMm1

        # Marks the eliminated range from front
        offset = -1

        # while there are elements to be inspected.
        # Note that we compare arr[fibMm2] with x.
        # When fibM becomes 1, fibMm2 becomes 0
        while (fibM > 1):

            # Check if fibMm2 is a valid location
            i = min(offset+fibMMm2, arr_len-1)

            # If x is greater than the value at
            # index fibMm2, cut the subarray array
            # from offset to i
            if (arr[i] < x):
                fibM = fibMMm1
                fibMMm1 = fibMMm2
                fibMMm2 = fibM - fibMMm1
                offset = i

            # If x is less than the value at
            # index fibMm2, cut the subarray
            # after i+1
            elif (arr[i] > x):
                fibM = fibMMm2
                fibMMm1 = fibMMm1 - fibMMm2
                fibMMm2 = fibM - fibMMm1

            # element found. return index
            else:
                return i

        # comparing the last element with x */
        if(fibMMm1 and arr[offset+1] == x):
            return offset+1

        # element not found. return -1
        return -1
