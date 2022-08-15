
def mergeSubarray(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    i = 0
    j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


if __name__ == "__main__":
    arr = [10, 15, 20, 11, 13]
    print(mergeSubarray(arr, 0, 2, 4))