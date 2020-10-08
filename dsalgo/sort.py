import sys

class Sort:
    def __new__(self, array, algo, reverse=False):
        """
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
        """
        self.array = array
        self.algo = algo
        self.reverse = reverse

        if self.algo == "bubble":
            return bubble(self.array, self.reverse)
        if self.algo == "merge":
            return merge(self.array, self.reverse)
        if self.algo == "bubble_recursion":
            return bubble_recursion(self.array, self.reverse)
        if self.algo == "selection":
            return selection(self.array, self.reverse)
        if self.algo == "quick":
            return quick(self.array, self.reverse)
        if self.algo == "radix":
            return radixSort(self.array, self.reverse)
        if self.algo == "bucket":
            return bucket_sort(self.array, self.reverse)
        if self.algo == "bitonic":
            return bitonic_sort(self.array, self.reverse)
        else:
            sys.stderr.write("Error: unsupported sorting algorithm passed!")


def bubble(array, reverse=False):
    """
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
    """
    n = len(array)
    for i in range(n):
        swap = 0
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = 1
        if swap == 0:
            break
    if reverse:
        return array[::-1]
    return array


def merge(array, reverse=False):
    """
    1.Divide:
    If q is the half-way point between p and r,
    then we can split the subarray A[p..r]
    into two arrays A[p..q] and A[q+1, r].
    2.Conquer:
    In the conquer step, we try to sort both
    the subarrays A[p..q] and A[q+1, r].
    If we haven't yet reached the base case,
    we again divide both these subarrays
    and try to sort them.
    3.Combine:
    When the conquer step reaches the base step and
    we get two sorted subarrays A[p..q] and A[q+1, r] for array A[p..r],
    we combine the results by creating a sorted array A[p..r]
    from two sorted subarrays A[p..q] and A[q+1, r].
     args:
      :array:(list) -> list to be sorted
      :reverse:(boolean) -> default = False,
                            can be True for sort
                            in reverse order
    """

    if len(array) > 1:
        mid = len(array) // 2  # mid
        left = array[:mid]  # Dividing the array elements
        right = array[mid:]  # into 2 halves

        merge(left)  # Sorting the first half
        merge(right)  # Sorting the second half
        i = j = k = 0

        # Copy data to left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    if reverse:
        return array[::-1]
    return array


def bubble_recursion(array, reverse=False):
    for i, num in enumerate(array):
        try:
            if array[i + 1] < num:
                array[i] = array[i + 1]
                array[i + 1] = num
                bubble_recursion(array)
        except IndexError:
            pass
    if reverse:
        return array[::-1]
    return array


def selection(array, reverse=False):
    """
    The selection sort algorithm sorts an array by repeatedly
    finding the minimum element (considering ascending order)
    from unsorted part and putting it at the beginning.
    The algorithm maintains two subarrays in a given array.
    1) The subarray which is already sorted.
    2) Remaining subarray which is unsorted.
    In every iteration of selection sort, the minimum element
    (considering ascending order)
    from the unsorted subarray is picked and moved to the sorted subarray.
    args:
      :array:(list) -> list to be sorted
      :reverse:(boolean) -> default = False,
                            can be True for sort
                            in reverse order
    """

    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]  # Swapping values

    if reverse:
        return array[::-1]

    return array


def quick(array, reverse=False):
    """The algorithm can be broken down into three parts​​:
    1.Partitioning the array about the pivot.
    2.Passing the smaller arrays to the recursive calls.
    3.Joining the sorted arrays that are returned from
    the recursive call and the pivot.

    args:
      :array:(list) -> list to be sorted
      :reverse:(boolean) -> default = False,
                            can be True for sort
                            in reverse order

    """
    start = 0
    end = len(array) - 1
    quick_sort(array, start, end)

    if reverse:
        return array[::-1]

    return array


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot)
        # and we can move left,
        # to the next element.
        # We also need to make sure we haven't
        # surpassed the low pointer, since that
        # indicates we have already moved all the elements
        # to their correct side of the pivot
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


def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array, reverse=False):
    """
    args:
      :array:(list) -> list to be sorted
      :reverse:(boolean) -> default = False,
                            can be True for sort
                            in reverse order
    """
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
    if reverse:
        return array[::-1]
    else:
        return array


def bucket_sort(arr, reverse=False):
    """Bucket Sort
    Complexity: O(n^2)
    The complexity is dominated by nextSort
    args:
      :array:(list) -> list to be sorted
      :reverse:(boolean) -> default = False,
                            can be True for sort
                            in reverse order
    """
    # The number of buckets and make buckets
    num_buckets = len(arr)
    buckets = [[] for bucket in range(num_buckets)]
    # Assign values into bucket_sort
    for value in arr:
        index = value * num_buckets // (max(arr) + 1)
        buckets[index].append(value)
    # Sort
    sorted_list = []
    for i in range(num_buckets):
        sorted_list.extend(next_sort(buckets[i]))
    if reverse:
        return sorted_list[::-1]
    else:
        return sorted_list


def next_sort(arr):
    # We will use insertion sort here.
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


def bitonic_sort(arr, reverse=False):
    """
    bitonic sort is sorting algorithm to use multiple process,
    but this code not containing parallel process
    It can sort only array that sizes power of 2
    It can sort array in both increasing order and decreasing order
    by giving argument true(increasing) and false(decreasing)

    Worst-case in parallel: O(log(n)^2)
    Worst-case in non-parallel: O(nlog(n)^2)

    args:
      :array:(list) -> list to be sorted,size of 2^N
      :reverse:(boolean) -> default = False,
                            can be True for sort
                            in reverse order
    """

    def compare(arr, reverse):
        n = len(arr) // 2
        for i in range(n):
            if reverse != (arr[i] > arr[i + n]):
                arr[i], arr[i + n] = arr[i + n], arr[i]
        return arr

    def bitonic_merge(arr, reverse):
        n = len(arr)

        if n <= 1:
            return arr

        arr = compare(arr, reverse)
        left = bitonic_merge(arr[: n // 2], reverse)
        right = bitonic_merge(arr[n // 2:], reverse)
        return left + right

    # end of function(compare and bitionic_merge) definition
    n = len(arr)
    if n <= 1:
        return arr
    # checks if n is power of two
    if not (n and (not (n & (n - 1)))):
        raise ValueError("the size of input should be power of two")

    left = bitonic_sort(arr[:n//2], True)
    right = bitonic_sort(arr[n//2:], False)

    arr = bitonic_merge(left + right, reverse)
    return arr
