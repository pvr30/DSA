def mergeArrayswithUnion(a, b):
    m, n = len(a), len(b)
    i = j = 0
    res = []

    while i < m and j < n:
        if a[i] < b[j]:
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
        elif a[i] > b[j]:
            if not res or res[-1] != b[j]:
                res.append(b[j])
            j += 1
        else:
            if not res or res[-1] == a[i]:
                res.append(a[i])
            i += 1
            j += 1

    while i < m:
        if not res or res[-1] != a[i]:
            res.append(a[i])
        i += 1
    while j < n:
        if not res or res[-1] != b[j]:
            res.append(b[j])
        j += 1

    return res

if __name__ == "__main__":
    a = [2, 3, 3, 3]
    b = [3, 4, 4]
    res = mergeArrayswithUnion(a, b)
    print(res)
