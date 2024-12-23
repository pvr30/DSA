"""
Check whether a number is a prime number or not.
A prime number is which have exact two factors 1 and a number itself.
"""

def isPrime1(n):
    """
    Time complexity is O(n)
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isPrime2(n):
    """Time complexity is O(sqrt(n))"""
    if n == 1:
        return False
    i = 2
    while i ** i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def isPrime3(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    print(isPrime1(13))
    print(isPrime1(14))

    print(isPrime2(13))
    print(isPrime2(14))

    print(isPrime3(13))
    print(isPrime3(14))
