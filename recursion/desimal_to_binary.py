def desimal_to_binary(n):
    if n == 0:
        return
    desimal_to_binary(n//2)
    print(n%2)

if __name__ == "__main__":
    desimal_to_binary(13)
