# String Validation
"""
Given a string s representing a password, you need to check if the string is valid or not. 
A valid string has the following properties:

String must have the length greater than or equal to 10.
String must contain at least 1 numeric character.
String must contain at least 1 uppercase character.
String must contain at least 1 lowercase character.
String must contain at least 1 special character from @#$-*.

Example 1:

Input: eHello123@
Output: 1
Explanation: String is valid.


Example 2:

Input: hella
Output: 0
Explanation: String is not valid.
"""



def validate(s):
    if len(s)<10:
        return 0
    count=0
    for i in s:
        if ord(i)>= 65 and ord(i)<=90:
            count=count+1
    if count==0:
        return 0
    a=0
    for j in s:
        if ord(j)>=97 and ord(j)<=122:
            a=a+1
    if a==0:
        return 0
    b=0
    for m in s:
        if m in "@#$-*":
            b=b+1
    if b==0:
        return 0
    k=0
    for l in s:
        if l.isnumeric()==True:
            k=k+1
    if k==0:
        return 0
    return 1


print(validate("eHello123@"))
print(validate("hella"))
