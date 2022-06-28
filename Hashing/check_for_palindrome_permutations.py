# Check For Palindrome Permutations

from collections import Counter


def is_palindrome_permutation(s):
    count_dict = Counter(s)
    odd = 0

    for freq in count_dict.values():
        if freq % 2 != 0:
            odd += 1
            if odd > 1:
                return False
    return True


print(is_palindrome_permutation("aba"))
print(is_palindrome_permutation("abaaac"))