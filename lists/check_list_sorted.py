def isListSorted(l):
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            return "No"
    return "Yes"

def isSorted(l):
    sorted_list = sorted(l)
    if l == sorted_list:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    ans = isListSorted([10, 5, 30])
    print(ans)

    ans = isSorted([10, 50, 300])
    print(ans)