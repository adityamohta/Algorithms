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


def partition(arr, begin, end, pivot_type="start"):
    if pivot_type == "start":
        pivot_index = begin
        for i in xrange(begin + 1, end + 1):
            if arr[i] <= arr[begin]:
                pivot_index += 1
                arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
        arr[pivot_index], arr[begin] = arr[begin], arr[pivot_index]
        return pivot_index

    elif pivot_type == "end":
        pivot_index = begin
        for i in xrange(begin, end):
            if arr[i] <= arr[end]:
                arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
                pivot_index += 1
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
        return pivot_index

    else:
        raise Exception("Enter a valid pivot_type")


def quick_sort(arr, begin=0, end=None):
    if end is None:
        end = len(arr) - 1

    def _quick_sort(arr, begin, end):
        if begin < end:
            pivot = partition(arr, begin, end, pivot_type="start")
            _quick_sort(arr, begin, pivot - 1)
            _quick_sort(arr, pivot + 1, end)

    return _quick_sort(array, begin, end)


if __name__ == '__main__':
    print "Unsorted array : ", array
    quick_sort(array)
    print "Sorted array : ", array
