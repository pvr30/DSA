def countVowels(s):
    c=0
    p = ["a","e","i","o","u"]
    s=set(s.lower())
    for i in s:
        if i in p:
            c=c+1
    return c

print(countVowels("vishaal"))