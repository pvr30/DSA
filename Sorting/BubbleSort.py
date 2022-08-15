"""
Bubble Sort is a sorting algorithm where we compare and swap the adjacent elements in an array.
Time Complexity: O(n^2)
"""


def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    

if __name__ == "__main__":
    arr = [3, 5, 1, 2, 4]
    bubbleSort(arr)
    print("After Sorting: ", arr)