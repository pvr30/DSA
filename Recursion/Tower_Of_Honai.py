# Tower Of Honai


def TOH(n, A, B, C):
    if n == 1:
        print(f"Move disk 1 from {A} to {C}")
    else:
        TOH(n-1, A, C, B)
        print(f"Move disk {n} from {A} to {C}")
        TOH(n-1, B, A, C)


# TOH(2, "A", "B", "C")
TOH(3, "A", "B", "C")