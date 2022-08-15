"""
make partition from given pivot and the left elements of pivot should be smaller and right elements
of the pivot should be bigger.
"""


def partion(arr, p):
    n = len(arr)
    arr[p], arr[n-1] = arr[n-1], arr[p]
    temp = []
    for i in range(n):
        if arr[i] <= arr[n-1]:
            temp.append(arr[i])
    for j in range(n):
        if arr[j] > arr[n-1]:
            temp.append(arr[j])
    for k in range(n):
        arr[k] = temp[k]


def hoarePartion(arr):
    pivot_index = 0
    pivot = arr[pivot_index]
    i = 0
    j = len(arr) - 1
    while i < j:
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[pivot_index] = arr[pivot_index], arr[j]


if __name__ == "__main__":
    arr = [5, 13, 6, 1, 3, 7, 2]
    partion(arr, 2)
    print(arr)
    hoarePartion(arr)
    print(arr)