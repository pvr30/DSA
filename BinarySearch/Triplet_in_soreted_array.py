"""
find the three elements which sum equal to given number
e.g. l = [2, 4, 8, 9, 11, 12, 20, 30],  s = 21
ans: [2, 8, 11]
"""


def pair_of_sum(l, s, start):
    start = start
    end = len(l) - 1

    while start < end:
        if l[start] + l[end] == s:
            return [l[start], l[end]]
        elif l[start] + l[end] < s:
            start += 1
        elif l[start] + l[end] > s:
            end -= 1
    return 0


def triplet(arr, x):
    for i in range(len(arr) - 2):
        res = pair_of_sum(arr, x-arr[i], i+1)
        if res:
            return res + [arr[i]]
    return 0


if __name__ == "__main__":
    print(triplet([2, 4, 8, 9, 11, 12, 20, 30], 21))
    # print(pair_of_sum([2, 4, 8, 9, 11, 12, 20, 30], 19))
    # print(pair_of_sum([2, 4, 8, 9, 11, 12, 20, 30], 34))
    # print(pair_of_sum([2, 4, 8, 9, 11, 12, 20, 30], 230))