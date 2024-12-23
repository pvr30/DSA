"""
Factorial of a number
"""

def factorial(n):
    if n == 0:
        return 0
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n-1)

if __name__ == "__main__":
    print(factorial(3))
    print(factorial(5))

    print(recursive_factorial(3))
    print(recursive_factorial(5))
    print(recursive_factorial(0))
