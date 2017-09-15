"""
    ---------- Quick Sort ----------
    1. Divide and Conquer
    2. Recursive
    3. Not Stable   (May change initial order of equal values)
    4. In-Place     (Space complexity is constant)
    
    5. Time complexity - 
        Best case - O(n log(n))
        Average case - O(n log(n))
        Worst case - O(n^2)
"""
from Array import array


def partition(array, begin, end, pivot_type="start"):
    if pivot_type == "start":
        pivotIndex = begin
        for i in xrange(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivotIndex += 1
                array[i], array[pivotIndex] = array[pivotIndex], array[i]
        array[pivotIndex], array[begin] = array[begin], array[pivotIndex]
        return pivotIndex

    elif pivot_type == "end":
        pivotIndex = begin
        for i in xrange(begin, end):
            if array[i] <= array[end]:
                array[i], array[pivotIndex] = array[pivotIndex], array[i]
                pivotIndex += 1
        array[pivotIndex], array[end] = array[end], array[pivotIndex]
        return pivotIndex

    else:
        raise Exception("Enter a valid pivot_type")


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin < end:
            pivot = partition(array, begin, end, pivot_type="start")
            _quicksort(array, begin, pivot - 1)
            _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)


if __name__ == '__main__':
    print "Unsorted Array : ", array
    quicksort(array)
    print "Sorted Array : ", array
