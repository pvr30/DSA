def getSecondLargest(l):
    if len(l) <= 1:
        return None
    
    lar = l[0]
    slar = None

    for x in l[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar is None or slar < x:
                slar = x
    return slar

if __name__ == "__main__":
    num = getSecondLargest([10, 20, 30, 30, 40])
    num2 = getSecondLargest([30, 2, 10, 15, 10])

    print(num)
    print(num2)