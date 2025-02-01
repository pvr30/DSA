"""
Time Complexity : O(logN)
"""
def binary_search(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == x:
            return mid
        elif l[mid] > x: # left side
            high = mid - 1
        elif l[mid] < x: # right side
            low = mid + 1
    return -1

def binary_search_recursive(l, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if l[mid] == x:
        return mid
    elif l[mid] > x:
        return binary_search_recursive(l, x, low, high-1)
    elif l[mid] < x:
        return binary_search_recursive(l, x, low+1, high)

if __name__ == "__main__":
    print(binary_search([10, 20, 30, 40, 50], 20))
    print(binary_search([10, 20, 30, 40, 50], 25))

    print(binary_search_recursive([10, 20, 30, 40, 50], 20, 0, 4))
    print(binary_search_recursive([10, 20, 30, 40, 50], 25, 0, 4))
