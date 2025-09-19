"""
Selection sort: In this algorithm we move the smallest element at first index and
keep doing it until the array is sorted.

This is not a stable algorithm.
"""
def selectionSort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_ind = i
        for j in range(i+1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]

    return arr

if __name__ == "__main__":
    arr = selectionSort([3, 2, 10, 1, 15, 7])
    arr1 = selectionSort([1, 2, 3, 4, 5])
    arr2 = selectionSort(["def", "gfg", "abc"])
    print(arr)
    print(arr1)
    print(arr2)
