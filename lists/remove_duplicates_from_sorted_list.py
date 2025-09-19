
def removeDuplicates(l):
    if not l:
        return l

    res = 1
    for i in range(1, len(l)):
        if l[res - 1] != l[i]:
            l[res] = l[i]
            res += 1
    return l[:res]


if __name__ == "__main__":
    ans = removeDuplicates([10, 20, 20, 30, 30, 30, 30])
    print(ans)
