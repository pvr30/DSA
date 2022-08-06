"""
find the pair which elements sum equal to given number
e.g. l = [2, 4, 8, 9, 11, 12, 20, 30],  s = 23
ans: [11, 12]
"""


def pair_of_sum(l, s):
    start = 0
    end = len(l) - 1

    while start < end:
        if l[start] + l[end] == s:
            return [l[start], l[end]]
        elif l[start] + l[end] < s:
            start += 1
        elif l[start] + l[end] > s:
            end -= 1
    return 0


if __name__ == "__main__":
    print(pair_of_sum([2, 4, 8, 9, 11, 12, 20, 30], 23))
    print(pair_of_sum([2, 4, 8, 9, 11, 12, 20, 30], 19))
    print(pair_of_sum([2, 4, 8, 9, 11, 12, 20, 30], 34))
    print(pair_of_sum([2, 4, 8, 9, 11, 12, 20, 30], 230))