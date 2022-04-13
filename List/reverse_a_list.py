# reverse a list
l = [10, 20, 30, 40, 50]
# l.reverse()
# print(l)
# print(list(reversed(l)))
# print(l[::-1])


def reverse_a_list(l):
    start = 0
    end = len(l) - 1
    while start < end:
        l[start], l[end] = l[end], l[start]
        start += 1
        end -= 1
    return l

print(reverse_a_list(l))