# sum of digits in a number

def sum_of_digits(n):
    if n < 10:
        return n
    return sum_of_digits(n // 10) + n % 10


print(sum_of_digits(123))
print(sum_of_digits(1111))