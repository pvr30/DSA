# find the subarray with 0 sum from an array


# TC = O(n^2)
def method1(l):
    n = len(l)
    for i in range(n):
        for j in range(i+1, n+1):
            if sum(l[i:j]) == 0:
                return True
    return False


# Hashing Method
def method2(l):
    prefix_sum = 0
    h = set()
    for i in range(len(l)):
        prefix_sum += l[i]
        if prefix_sum == 0 or prefix_sum in h:
            return True
        h.add(prefix_sum)
    return False


print(method1([-3, 4, -3, -1, 1]))
print(method2([-3, 4, -3, -1, 1]))