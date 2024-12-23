"""
Find the greatest common divisor of two numbers.
"""

# Euclidean algorithm solution 1
def gcd1(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

"""
Euclidean algorithm solution 2
gcd(a, b) = gcd(a-b, b) where a > b

greater % smaller and if one of them is 0 then other is gcd.
"""
def gcd2(a, b):
    if b == 0:
        return a
    return gcd2(b, a % b)

if __name__ == "__main__":
    print(gcd1(4,6))
    print(gcd1(100,200))

    print(gcd2(4, 6))
    print(gcd2(100, 200))
