"""
Bubble sort: In this sorting algorithm we move the largest element
at last index by comparing adjacent elements from an array.

This sorting algorithm is stable
"""
def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        sorted = False
        for j in range(n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = True
        if not sorted:
            return arr
    return arr

if __name__ == "__main__":
    arr = bubbleSort([3, 2, 10, 1, 15, 7])
    arr1 = bubbleSort([1, 2, 3, 4, 5])
    arr2 = bubbleSort(["def", "gfg", "abc"])
    print(arr)
    print(arr1)
    print(arr2)
