def sqrt_of_N(n):
    low = 1
    high = n
    ans = -1

    while low <= high:
        mid = (low+high) // 2
        if (mid * mid) <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

if __name__ == "__main__":
    print(sqrt_of_N(25))
    print(sqrt_of_N(30))
