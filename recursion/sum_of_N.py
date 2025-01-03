def sum_of_N(n):
    if n < 10:
        return n
    return sum_of_N(n // 10) + (n % 10)

if __name__ == "__main__":
    print(sum_of_N(234))