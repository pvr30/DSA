def isPalindromeString(s, start, end):
    if start >= end:
        return True
    return s[start] == s[end] and isPalindromeString(s, start+1, end-1)

s = "abba"
print(isPalindromeString(s, 0, len(s) - 1))