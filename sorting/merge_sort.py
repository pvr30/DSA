"""
Merge sort is merge two sorted array recursively.
"""
from sorting.merge_subarray import merge

def mergeSort(arr, l, r):
    if r > l:
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

if __name__ == "__main__":
    a = [10, 15, 20, 40, 8, 11, 55]
    mergeSort(a, 0, len(a))
    print(a)
