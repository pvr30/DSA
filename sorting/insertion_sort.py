"""
Insertion Sort Algorithm

The insertion sort algorithm, which is a simple
sorting technique that builds the sorted array one item at a time. It
compares each element with the ones before it and inserts it into its
correct position.
"""
def insertionSort(arr):
    n = len(arr)

    for i in range(n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr

if __name__ == "__main__":
    arr = insertionSort([3, 2, 10, 1, 15, 7])
    arr1 = insertionSort([1, 2, 3, 4, 5])
    arr2 = insertionSort(["def", "gfg", "abc"])
    print(arr)
    print(arr1)
    print(arr2)
