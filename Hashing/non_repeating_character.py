"""
Given a string S consisting of lowercase Latin Letters. Return the first non-repeating character in S.
If there is no non-repeating character, return '$'.

Example 1:

Input:
S = hello
Output: h
Explanation: In the given string, the
first character which is non-repeating
is h, as it appears first and there is
no other 'h' in the string.
"""

from collections import OrderedDict, Counter


def non_repeating_char(s):
    # solution 1

    # str_dict = OrderedDict()
    # for i in s:
    #     try:
    #         str_dict[i] += 1
    #     except KeyError:
    #         str_dict[i] = 1
    # for i in str_dict:
    #     if str_dict[i] == 1:
    #         return i

    # solution 2
    freq = Counter(s)
    for i in s:
        if freq[i] == 1:
            return i

    return '$'


if __name__ == '__main__':
    print(non_repeating_char("hello"))
    print(non_repeating_char("zxvczbtxyzvy"))
