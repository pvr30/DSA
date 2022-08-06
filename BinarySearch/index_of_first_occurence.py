#  find the index of first occurence in a list
"""
e.g. l = [1, 10, 10, 20, 20, 20], x = 20
ans:- 3
"""


# O(N)
def firstIndex(l, x):
    for i in range(len(l)):
        if l[i] == x:
            return i
    return -1


# O(logN)
def firstIndexBS(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low+high) // 2
        if x > l[mid]:
            low = mid + 1
        elif x < l[mid]:
            high = mid - 1
        else:
            if mid == 0 or l[mid-1] != l[mid]:
                return mid
            else:
                high = mid - 1
    return -1


if __name__ == "__main__":
    print(firstIndex([1, 10, 10, 20, 20, 20], 20))
    print(firstIndex([5, 10, 10, 20, 20], 10))

    print()
    
    print(firstIndexBS([1, 10, 10, 20, 20, 20], 20))
    print(firstIndexBS([5, 10, 10, 20, 20], 10))