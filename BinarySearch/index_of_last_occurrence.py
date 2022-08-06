#  find the index of last occurrence in a list
"""
e.g. l = [1, 10, 10, 20, 20, 20], x = 20
ans:- 5
"""


# O(N)
def lastIndex(l, x):
    for i in reversed(range(len(l))):
        if l[i] == x:
            return i
    return -1


# O(logN)
def lastIndexBS(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if x > l[mid]:
            low = mid + 1
        elif x < l[mid]:
            high = mid - 1
        else:
            if mid == len(l) - 1 or l[mid + 1] != l[mid]:
                return mid
            else:
                low = mid + 1
    return -1


if __name__ == "__main__":
    print(lastIndex([1, 10, 10, 20, 20, 20], 20))
    print(lastIndex([5, 10, 10, 20, 20], 10))

    print()

    print(lastIndexBS([1, 10, 10, 20, 20, 20], 20))
    print(lastIndexBS([5, 10, 10, 20, 20], 10))