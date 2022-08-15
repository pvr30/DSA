"""
Find the minimum difference in an array.
e.g. arr = [1, 8, 12, 5, 18]
    ans: 3

"""

# Naive Solution
def mindiff(arr):
    min_diff = float("inf")
    for i in range(1, len(arr)):
        for j in range(i):
            if abs(arr[i] - arr[j]) < min_diff:
                min_diff = abs(arr[i] - arr[j])
    print(min_diff)


# Efficient Solution, Time Complexity: O(NlogN)
def minDiff(arr):
    arr.sort()
    min_diff = float("inf")
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) < min_diff:
            min_diff = abs(arr[i] - arr[i+1])
    print(min_diff)


if __name__ == "__main__":
    arr = [1, 8, 12, 5, 18]
    mindiff(arr)
    arr = [20, 10, 3, 12]
    minDiff(arr)