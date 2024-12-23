from mathematics.prime_number import isPrime1

def prime_factorization(n):
    if n == 1:
        print(1)

    for i in range(2, n+1):
        if isPrime1(i):
            x = i
            while n % x == 0:
                print(i)
                x = x * i

if __name__ == "__main__":
    prime_factorization(15)
    prime_factorization(100)
    prime_factorization(13)
