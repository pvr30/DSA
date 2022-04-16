str = "madam"

# solution 2
def palindrome1(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            print("No")
            break
        start += 1
        end -= 1
    else:
        print("Yes")

# solution 2
def palindrome2(s):
    if s == s[::-1]:
        print('Yes')
    else:
        print("No")

palindrome1(str)
palindrome2(str)

