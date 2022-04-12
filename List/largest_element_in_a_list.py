# find the largest element from the array

l = [10, 20, 5, 50]
print(max(l))

# Time Complexity: O(n^2)
def get_largest_ele(l):
    for x in l:
        for y in l:
            if y > x:
                break
        else:
            return x
    return None

print(get_largest_ele(l))


# Efficient Solution - O(n)

def get_largest__element_efficient_way(l):
    if l is None:
        return None
    else:
        res = l[0]
        for i in range(1, len(l)):
            if l[i] > res:
                res = l[i]
        return res

print(get_largest__element_efficient_way(l))