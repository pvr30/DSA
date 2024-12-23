"""
Find sum of N natural numbers.
"""

def sum(n):
    # s = 0
    # for i in range(1, n+1):
    #     s += i
    # return s

    # Formula for this
    return n * (n+1)//2

if __name__ == "__main__":
    print(sum(2))
    print(sum(10))
