"""
Find the median of two sorted array.

"""
# Naive Solution
def getMedian(a1, a2):
    temp = a1 + a2
    temp = sorted(temp)
    if len(temp) % 2 != 0:
        return temp[len(temp) // 2]
    else:
        mid = len(temp) // 2
        return (temp[mid] + temp[mid - 1]) / 2


# solution using binary search
def getMedianBS(a1, a2):
    n1, n2 = len(a1), len(a2)
    b1, e1 = 0, n1
    while b1 <= e1:
        i1 = (b1 + e1) // 2
        i2 = (n1 + n2 + 1) // 2 - i1
        r1 = float("inf") if i1 == n1 else a1[i1]
        l1 = float("-inf") if i1 == 0 else a1[i1 - 1]
        r2 = a2[i2]
        l2 = a2[i2 - 1]
        if l1 <= r2 and l2 <= r1:
            if (n1 + n2) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return max(l1, l2)
        elif l1 > r2:
            e1 = i1 - 1
        else:
            b1 = i1 + 1


if __name__ == "__main__":
    print(getMedian([10, 20, 30], [5, 15, 25, 35, 45]))
    print(getMedianBS([10, 20, 30], [5, 15, 25, 35, 45]))
