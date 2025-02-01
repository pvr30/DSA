"""
Upper bound is the smallest element which is greater than to x
"""

def upperBound(arr, x):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

if __name__ == "__main__":
    ans = upperBound([1, 2, 3, 3, 5, 8, 10, 10, 11], 3)
    print(ans)