"""
Count the number of possible triangles:
Given an unsorted array arr[] of n positive integers. Find the number of triangles that can be formed with three
different array elements as lengths of three sides of triangles.

Example 1:

Input:
n = 3
arr[] = {3, 5, 4}
Output:
1
Explanation:
A triangle is possible
with all the elements 5, 3 and 4.
Example 2:

Input:
n = 5
arr[] = {6, 4, 9, 7, 8}
Output:
10
Explanation:
There are 10 triangles
possible  with the given elements like
(6,4,9), (6,7,8),...

"""


def findNumberOfTriangles(arr):
    # code here
    arr.sort()
    i = len(arr) - 1
    count = 0
    while i:
        l = 0
        r = i - 1
        while l < r:
            if arr[l] + arr[r] > arr[i]:
                count += (r - l)
                r -= 1
            else:
                l += 1
        i -= 1
    return count


if __name__ == "__main__":
    print(findNumberOfTriangles([6, 4, 9, 7, 8]))