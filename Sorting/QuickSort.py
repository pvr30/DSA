"""
Quick Sort: QuickSort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array
around the picked pivot.
    -Always pick the first element as a pivot.
    -Always pick the last element as a pivot (implemented below)
    -Pick a random element as a pivot.
    -Pick median as the pivot.

In simple terms put the smaller elements than pivot on left side of array and put larger elements than pivot on right
side of the array, do this process recursively.

Time Complexity: O(NlogN)
"""


def partition(arr, l, h):
    pivot_index = l
    pivot = arr[pivot_index]
    i, j = l, h
    # loop continued until j cross the i
    while i < j:
        # increment left side means i until we find element which is larger than pivot
        while arr[i] <= pivot:
            i += 1
        # increment right side means j until we find element which is smaller than pivot
        while arr[j] > pivot:
            j -= 1

        if i < j:
            # swap i and j element when we find arr[i] is large and arr[j] is small
            arr[i], arr[j] = arr[j], arr[i]

    # finally put the pivot on its right position
    arr[j], arr[pivot_index] = arr[pivot_index], arr[j]
    return j


def quickSort(arr, l, h):
    if l < h:
        p = partition(arr, l, h)  # get pivot index from partition function
        quickSort(arr, l, p-1)  # left side of partition
        quickSort(arr, p+1, h)  # right side of partition


# Tail Call Elimination to reduce recursive call

def qSort(arr, l , h):
    while l < h:
        p = partition(arr, l, h)
        quickSort(arr, l, p - 1)
        l = p + 1


if __name__ == "__main__":
    arr = [5, 6, 20, 1, 2, 25, 15]
    quickSort(arr, 0, len(arr)-1)
    print("After sorting ", arr)
    qSort(arr, 0, len(arr)-1)
