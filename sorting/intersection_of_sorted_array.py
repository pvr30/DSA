def intersectionArrays(a, b):
    m, n = len(a), len(b)
    i = j = 0
    res = []

    while i < m and j < n:
        if a[i] == b[j]:
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    return res


if __name__ == "__main__":
    a = [2, 3, 3, 3, 4, 5]
    b = [3, 3, 4, 5]

    res = intersectionArrays(a, b)
    print(res)
