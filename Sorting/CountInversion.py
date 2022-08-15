"""
Count Inversion Problem: find the count of a larger element appear before smaller element in an array.
e.g. arr = [2, 5, 8, 11, 3, 6, 9, 13]
    ans: 6

"""

# Naive Solution  , Time Complexity: O(n^2)
def countInversionNaivesolution(arr):
    n = len(arr)
    res = 0
    for i in range(n-1):
        for j in range(i+1, n-1):
            if arr[i] > arr[j]:
                res += 1
    return res


# Solution Using Merge Sort, Time Complexity: O(NlogN)

def countMerge(arr, left, mid, right):
    left_array = arr[left:mid+1]
    right_array = arr[mid+1:right+1]

    res, i, j, k = 0, 0, 0, left
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
            k += 1
        else:
            arr[k] = right_array[j]
            j += 1
            k += 1
            res += (len(left_array) - i)
    while i < len(left_array):
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        arr[k] = right_array[j]
        j += 1
        k += 1
    return res


def invCount(arr, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += invCount(arr, left, mid)
        count += invCount(arr, mid+1, right)
        count += countMerge(arr, left, mid, right)
    return count


if __name__ == "__main__":
    arr = [2, 5, 8, 11, 3, 6, 9, 13]
    print(countInversionNaivesolution(arr))
    print(invCount(arr, 0, len(arr)))