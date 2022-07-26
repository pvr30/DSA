# Tower Of Honai


def TOH(n, A, B, C):
    if n == 1:
        print(f"Move disk 1 from {A} to {C}")
        return 1
    else:
        i = TOH(n-1, A, C, B)
        print(f"Move disk {n} from {A} to {C}")
        i = i + TOH(n-1, B, A, C)
        return i+1


print(TOH(2, "A", "B", "C"))
print()
print(TOH(3, "A", "B", "C"))