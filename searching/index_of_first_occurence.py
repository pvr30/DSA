def firstOccurence(arr, x):
    low = 0
    high = len(arr) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return first

if __name__ == "__main__":
    print(firstOccurence([10, 20, 20, 30, 40, 40, 40, 50], 40))