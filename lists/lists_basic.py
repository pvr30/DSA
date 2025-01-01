if __name__ == "__main__":
    l = [10, 20, 30, 40, 50]
    l.append(30)
    print(l)
    l.insert(1, 15)
    print(l)
    print(l.count(30))
    print(l.index(30))
    print(l.index(30, 4, 7))

    print(l.pop())
    print(l.pop(1))
    del l[1]
    print(l)
    del l[0:2]
    print(l)

    l.reverse()
    print(l)
    l.sort()
    print(l)

    l = [10, 20, 30, 40, 50]
    print(l[4:1:-1]) # list[start:stop:step]
    print(l[::-1])
