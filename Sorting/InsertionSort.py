"""
    1. Start Picking Elements one by one from the left.
    2. Shift all those elements by one position to the right which 
       are greater then the current element and are on left side of it.
    3. Insert when all the values on the left of it are smaller than the current number.
    
    Time Complexity - 
        best case       -   O(n)
        average case    -   O(n^2)
        worst case      -   O(n^2)
    
    Insertion Sort is a STABLE sorting algorithm, i.e. if it encounters 2 equal values, 
    it doesn't change its initial order after sorting.
"""
from Array import array


def insertion_sort(arr, size):
    for i in range(1, size - 1):
        value = arr[i]
        hole = i

        while hole > 0 and arr[hole - 1] > value:
            arr[hole] = arr[hole - 1]       # Shifting values to the right one by one
            hole = hole - 1                 # Moving from current element to 1st element (right to left direction)

        arr[hole] = value


if __name__ == '__main__':
    print "Unsorted Array : ", array
    insertion_sort(array, len(array))
    print "Sorted Array : ", array
