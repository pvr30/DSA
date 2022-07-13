"""
- Josephus Problem

There are N people standing in a circle numbered from 1 to N. Also given an integer K.
First, count the K-th number starting from the first one and delete it. Then K numbers are counted starting from the
next one and the K-th one is removed again, and so on. The process stops when one number remains.
The task is to find the last number.


"""


def JOS(n, k):
    if n == 1:
        return 0
    return (JOS(n-1, k) + k) % n


print(JOS(5, 2))
print(JOS(7, 3))
print(JOS(6, 2))