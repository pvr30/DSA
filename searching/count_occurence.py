from index_of_first_occurence import firstOccurence
from index_of_last_occurence import lastOccurence

def countOccurence(arr, x):
    first = firstOccurence(arr, x)
    last = lastOccurence(arr, x)

    if first == -1:
        return 0

    return (last - first) + 1

if __name__ == "__main__":
    print(countOccurence([10, 20, 20, 30, 40, 40, 40, 50], 40))
