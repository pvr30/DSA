"""
Given an array a[ ] of size N. The task is to check if array is sorted or not. A sorted array can either be increasingly sorted or decreasingly sorted. Also consider duplicate elements to be sorted.

Example 1:

Input:
N = 5
a[] = {1, 1, 2, 2, 3}
Output:
1
Explanation:
Here, Given array a is increasingly sorted.
Example 2:

Input:
N = 2
a[] = {4, 2}
Output:
1
Explanation:
Here, Given array a is decreasingly sorted.
"""


def is_sorted(arr):
    is_increasing = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    is_decreasing = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

    if is_increasing or is_decreasing:
        return 1
    else:
        return 0

if __name__ == "__main__":
    arr1 = [4, 2]
    arr2 = [6, 9, 6, 9, 3, 2, 8, 9, 3]

    print(is_sorted(arr1))
    print(is_sorted(arr2))
