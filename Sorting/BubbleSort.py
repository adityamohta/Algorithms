"""
    ---------- Bubble Sort ----------
    Time Complexity - 
        best case       -   O(n)
        average case    -   O(n^2)
        worst case      -   O(n^2)
"""

from Array import array


def bubble_sort(arr, begin=0, end=None):
    if end is None:
        end = len(arr) - 1

    for i in range(begin, end):
        swapped = False
        for j in range(begin, end - i):
            if array[j] >= array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    print "Unsorted Array : ", array
    bubble_sort(array)
    print "Sorted Array : ", array
