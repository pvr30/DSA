from index_of_first_occurence import firstIndexBS
from index_of_last_occurrence import lastIndexBS


def countOcuc(l, x):
    first = firstIndexBS(l, x)
    if first == -1:
        return 0
    return lastIndexBS(l, x) - first + 1


if __name__ == '__main__':
    print(countOcuc([10, 20, 20, 20, 30, 30], 10))
    print(countOcuc([10, 20, 20, 20, 30, 30], 20))
    print(countOcuc([10, 20, 20, 20, 30, 30], 30))
