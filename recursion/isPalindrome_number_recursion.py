def isPalindrome(N):
    rev = helper(N)
    if rev == N:
        return True
    else:
        return False

def helper(n, temp=0):
    if n == 0:
        return temp
    temp = (temp * 10) + (n % 10)
    return helper(n // 10, temp)

if __name__ == "__main__":
    print(isPalindrome(121))
    print(isPalindrome(12))
