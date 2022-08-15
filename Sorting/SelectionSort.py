"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

The subarray which is already sorted. 
Remaining subarray which is unsorted.

Time Complexity: O(n^2)

"""


def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            # if arr[j] > arr[min_index]:  # descending order
            if arr[j] < arr[min_index]:  # ascending order
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    arr = [3, 5, 1, 2, 4]
    selectionSort(arr)
    print("After Sorting: ", arr)