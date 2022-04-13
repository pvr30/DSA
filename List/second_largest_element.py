# find the second largest element in a list

l = [10, 12, 40, 20, 50]

# Naive Solution (Two Traversal) - O(n)
def get_sec_lar_ele(l):
    if l is None:
        return None
    else:
        lar = max(l)
        slar = None

        for x in l:
            if x != lar:
                if slar == None:
                    slar = x
                else:
                    slar = max(slar, x)
        return slar

print(get_sec_lar_ele(l))

l = [10, 10, 5]
# efficent solution
def get_sec_max(l):
    if len(l) <= 1:
        return None
    lar = l[0]
    slar = None

    for x in l:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar == None or slar < x:
                slar = x
    return slar


print(get_sec_max(l))