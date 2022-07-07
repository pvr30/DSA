def dtbfun(n):
    if n > 1:
        dtbfun(n//2)
    print(n % 2, end="")


dtbfun(13)
print()
dtbfun(15)