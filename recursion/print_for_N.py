def print1toN(n):
    if n<=0:
        return
    printNto1(n-1)
    print(n)

def printNto1(n):
    if n<=0:
        return
    print(n)
    printNto1(n-1)

if __name__ == "__main__":
    print1toN(5)
    print("---")
    printNto1(5)