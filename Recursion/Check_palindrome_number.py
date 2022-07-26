# Check weather a number is palindrome or not

# e.g 101, 1001

def isPalindrome(n):
    res = helper(n, 0)
    if res == n:
        print("given number is palindrome")
    else:
        print("given number is not palindrome")


def helper(n, temp):
    if n == 0:
        return temp

    temp = (temp * 10) + (n % 10)

    return helper(n // 10, temp)


if __name__ == "__main__":
    isPalindrome(100)
    isPalindrome(101)