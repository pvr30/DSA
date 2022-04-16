"""
An anagram of a string is another string that contains the same characters, 
only the order of characters can be different. 
For example, “abcd” and “dabc” are an anagram of each other.
"""
s1 = "abcd"
s2 = "dabc"


# naive solution
def anagram1(s1, s2):
    if len(s1) != len(s2):
        return False
    return(sorted(s1) == sorted(s2))

# efficient solution
def anagram2(s1, s2):
    if len(s1) != len(s2):
        return False
    count = [0] * 256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    for x in count:
        if x != 0:
            return False
    return True

print(anagram1(s1, s2))
print(anagram2(s1, s2))
