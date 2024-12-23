"""
Check a number is palindrome or not.
"""

def is_palindrome(n):
    rev = 0
    temp = n
    while temp > 0:
        last_digit = temp % 10
        rev = rev * 10 + last_digit # in this equation we need to somehow add 0 to rev value and add last_digit value.
        temp = temp // 10
    return n == rev

if __name__ == "__main__":
    print(is_palindrome(121))
    print(is_palindrome(12))
