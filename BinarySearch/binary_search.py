"""

Binary Search is a searching algorithm used in a sorted array by repeatedly dividing
the search interval in half. The idea of binary search is to use the information that
the array is sorted and reduce the time complexity to O(Log n).

"""


def binarysearch(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if x == l[mid]:
            return mid
        elif x > l[mid]:
            low = mid + 1
        elif x < l[mid]:
            high = mid - 1

    return -1

# recursive solution of binary search


def bsearch(l, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if x == l[mid]:
        return mid
    elif x > l[mid]:
        return bsearch(l, x, mid + 1, high)
    elif x < l[mid]:
        return bsearch(l, x, low, high - 1)


def bsearchMain(l, x):
    return bsearch(l, x, 0, len(l) - 1)


if __name__ == "__main__":
    print(binarysearch([1, 2, 3, 4, 5], 3))
    print(binarysearch([1, 2, 3, 4, 5], 10))

    print(bsearchMain([1, 2, 3, 4, 5], 3))
    print(bsearchMain([1, 2, 3, 4, 5], 10))

