
from cmath import sqrt


def fun(arr):
    temp_set = set(arr)
    print(len(temp_set))
    count_dict = {}
    for i in arr:
        count_dict[i] = arr.count(i)
    print(count_dict)
    return max(zip(count_dict.values(), count_dict.keys()))[1]


if __name__ == '__main__':
    print(fun([3, 1, 3, 3, 2, 1, 1, 1]))