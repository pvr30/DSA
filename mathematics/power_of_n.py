def power1(x, n):
    res = 1
    for i in range(0, n):
        res = res * x
    print(res)

def power2(x, n):
    if n == 0:
        return 1
    temp = power2(x, n//2)
    temp = temp * temp
    if n % 2 == 0:
        return temp
    else:
        return temp * x

if __name__ == "__main__":
    power1(3, 3)

    print(power2(3, 4))