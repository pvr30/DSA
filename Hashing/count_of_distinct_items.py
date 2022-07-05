# Find out the count of distinct items in a list

def count_distinct_method1(l):
    res = 0
    for i in range(0, len(l)):
        if l[i] not in l[0:i]:
            res += 1
    return res


def count_distinct_method2(l):
    return len(set(l))


print(count_distinct_method1([10, 20, 10, 30, 20]))
print(count_distinct_method2([10, 20, 10, 30, 20]))


