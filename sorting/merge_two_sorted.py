def mergeArrays(a, b):
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    res = []

    while i < m and j < n:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while i < m:
        res.append(a[i])
        i += 1
    while j < n:
        res.append(b[j])
        j += 1

    return res

if __name__ == "__main__":
    a = [1, 2, 4, 7, 9]
    b = [3, 8, 10]

    res = mergeArrays(a, b)
    print(res)
