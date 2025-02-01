def lastOccurence(arr, x):
    low = 0
    high = len(arr) - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] > x:
            high = low - 1
        else:
            low = mid + 1
    return last

if __name__ == "__main__":
    print(lastOccurence([10, 20, 20, 30, 40, 40, 40, 50], 40))