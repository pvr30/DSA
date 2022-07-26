
def fun(n, p):
    if p == 1:
        return n
    return fun(n, p-1) * n

if __name__ == '__main__':
    print(fun(9, 9))