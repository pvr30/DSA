
def leftRotateByOne(l):
    x = l[0]
    for i in range(1, len(l)):
        l[i-1] = l[i]
    l[len(l) - 1] = x
    return l

if __name__ == "__main__":
    ans = leftRotateByOne([10, 20, 30, 40, 50])
    print(ans)
