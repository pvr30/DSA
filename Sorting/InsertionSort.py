"""
Insertion sort :-
    - divine the given array into two parts
    - take first element from unsorted array and find its correct
        position in sorted array
    - repeat until unsorted array is empty

Time Complexity: O(n^2)
"""


def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        x = arr[i]
        j = i - 1
        while j >= 0 and x < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = x


if __name__ == "__main__":
    arr = [3, 5, 1, 2, 4]
    insertionSort(arr)
    print("After Sorting: ", arr)
