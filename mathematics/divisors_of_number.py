
def printDivisors1(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

def printDivisors2(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
        i += 1
    while i >= 1:
        if n % i == 0:
            if i != n // i:
                print(n//i)
        i -= 1

if __name__ == "__main__":
    printDivisors1(100)
    printDivisors1(13)

    print()

    printDivisors2(25)
