"""
    ---------- Selection Sort ----------
    Time Complexity - 
        best case       -   O(n^2)
        average case    -   O(n^2)
        worst case      -   O(n^2)
"""
from Array import array


def selection_sort(arr, begin=0, end=None):
    if end is None:
        end = len(arr) - 1
    for i in range(begin, end):
        min_index = i
        for j in range(i + 1, end + 1):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


if __name__ == '__main__':
    print "Unsorted Array : ", array
    selection_sort(array)
    print "Sorted Array : ", array
