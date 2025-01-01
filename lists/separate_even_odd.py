
def even_odd_lists(l):
    even = []
    odd = []
    for ele in l :
        if ele % 2 == 0:
            even.append(ele)
        else:
            odd.append(ele)
    return even, odd

if __name__ == "__main__":
    even, odd = even_odd_lists([10, 11, 12, 13, 14])
    print(even, odd)
