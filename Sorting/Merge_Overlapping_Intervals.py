"""
Merge Overlapping Intervals:

Input: Intervals = {{1,3},{2,4},{6,8},{9,10}}
Output: {{1, 4}, {6, 8}, {9, 10}}
Explanation: Given intervals: [1,3],[2,4],[6,8],[9,10], we have only two overlapping intervals here,
[1,3] and [2,4]. Therefore we will merge these two and return [1,4],[6,8], [9,10].

Input: Intervals = {{6,8},{1,9},{2,4},{4,7}}
Output: {{1, 9}}
"""


def mergeIntervals(arr):
    arr.sort(key=lambda x: x[0])
    res = 0
    for i in range(1, len(arr)):
        if arr[res][1] >= arr[i][0]:
            arr[res][1] = max(arr[res][1], arr[i][1])
        else:
            res = res + 1
            arr[res] = arr[i]

    for i in range(res + 1):
        print(arr[i], end=" ")


if __name__ == "__main__":
    arr = [[5, 10], [3, 15], [18, 30], [2, 7]]
    mergeIntervals(arr)
