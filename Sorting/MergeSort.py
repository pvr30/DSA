"""
Merge Sort: Divide the array into two halves and sort them, after sorting merge them.
Time Complexity: O(NlogN)
"""


def merge(arr, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    merge(arr, left, right)


if __name__ == "__main__":
    arr = [5, 6, 1, 2, 7, 3, 4]
    mergeSort(arr)
    print("After Sorting:", arr)