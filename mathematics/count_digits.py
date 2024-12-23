"""
Count number of digits in a number.
"""

def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

if __name__ == "__main__":
    print(count_digits(3))
    print(count_digits(32123))
    print(count_digits(123456789))
