# find GCD/HCF of two numbers


def fun(a, b):
    res = min(a, b)

    ans = None
    for i in range(1, res + 1):
        if a % res == 0 and b % res == 0:
            ans = i
    return ans

# using recursion
def funrecursive(a, b):
    if b == 0:
        return a
    return fun(b, a % b)


if __name__ == '__main__':
    print(fun(30, 60))
    print(funrecursive(30, 60))
