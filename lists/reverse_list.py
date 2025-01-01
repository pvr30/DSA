def reverse_list(l):
    i = 0
    j = len(l) - 1
    while i != j:
        l[i], l[j] = l[j], l[i]
        i+=1
        j-=1
    return l

    # return l[::-1]

if __name__ == "__main__":
    l = reverse_list([10, 20, 30, 40, 30])
    print(l)