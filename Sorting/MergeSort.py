"""
    ---------- Merge Sort ----------
    1. Divide and Conquer
    2. Recursive
    3. Stable   (doesn't change initial order of equal values)
    4. Not In-Place     (Space complexity is not constant. O(n) for array version, O(log(n)) for linked list version)
    5. O(n log(n)) time complexity for all cases (best, average, worst)
"""
from Array import array


def merge(arr, start, mid, end):
    left_arr_size = mid - start + 1
    right_arr_size = end - mid

    # Create temp arrays
    left_arr = [0] * left_arr_size
    right_arr = [0] * right_arr_size

    # Copy data to temp arrays left_arr[] and right_arr[]
    for i in range(0, left_arr_size):
        left_arr[i] = arr[start + i]

    for j in range(0, right_arr_size):
        right_arr[j] = arr[mid + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = start  # Initial index of merged subarray

    while i < left_arr_size and j < right_arr_size:
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    # Copy the remaining elements of left_arr[], if there are any
    while i < left_arr_size:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    # Copy the remaining elements of right_arr[], if there are any
    while j < right_arr_size:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr, start, end):

    if start < end:
        mid = int((start + end) / 2)  # middle position.

        # Sort first and second halves
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


if __name__ == '__main__':
    print "Unsorted Array : ", array
    merge_sort(array, 0, len(array) - 1)
    print "Sorted Array : ", array
