
# find sum of N natural numbers

def sum_N_numbers_equation_method(n):
    return n * (n+1)//2


def sum_N_numbers(n):
    if n == 0:
        return n
    return n + sum_N_numbers(n-1)


print(sum_N_numbers_equation_method(10))
print(sum_N_numbers(10))

