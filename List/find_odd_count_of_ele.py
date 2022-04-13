# find the odd count of elements in an array

l = [10, 20, 10, 10, 20, 40, 40]


def find_odd_count(l):
    res = None
    for x in l:
        count = l.count(x)
        if count % 2 != 0:
            res = x
            break
    return res

print(find_odd_count(l))