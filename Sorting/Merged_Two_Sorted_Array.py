"""

Merge Two Sorted Array.
Time Complexity:  O(m+n)

"""


def mergeSortedArray(a, b):
    res = []
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    while i < m and j < n:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < m:
        res.append(a[i])
        i += 1
    while j < n:
        res.append(b[j])
        j += 1
    return res


if __name__ == "__main__":
    a = [1, 2, 5, 6]
    b = [2, 4, 10]
    print(mergeSortedArray(a, b))