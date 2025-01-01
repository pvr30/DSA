def largest_element(l):
    if not l:
        return None

    largest_num = l[0]
    for i in l[1:]:
        if i > largest_num:
            largest_num = i
    return largest_num


if __name__ == "__main__":
    num = largest_element([10, 20, 30, 30, 40])
    print(num)
