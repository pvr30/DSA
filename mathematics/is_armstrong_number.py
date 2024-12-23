"""
Check a number is an armstrong number or not.
Armstrong number is a number that is equal to the sum of cubes of its digits.
"""

def is_armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        last_digit = temp % 10
        sum += (last_digit * last_digit * last_digit)
        temp = temp // 10
    return n == sum

if __name__ == "__main__":
    print(is_armstrong(153))
    print(is_armstrong(15))
