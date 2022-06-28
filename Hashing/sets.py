"""
- Sets in Python
 - Distinct Element
 - Unordered
 - No Indexing
 - Union, Intersection, Self Difference etc are Fast
 - Sets using hashin internally

"""

# s1 = {}  # this is dictionary not set

# s = set()
s1 = {1, 3, 7}

s2 = set([3, 4, 9])

s1.add(2)

s1.update([6, 3, 5])

s2.update({10, 20}, [3, 5])

print(s1)
print(s2)

s1.remove(5)  # remove does give error is element is not present

s1.remove(1)

s2.discard(20)  # discard does not raise error if element is not present

s2.discard(10)

print(s1)
print(s2)


print("\n Set Operation")

print(s1 | s2)  # print(s1.union(s2))
print(s1 & s2)  # print(s1.intersection(s2))
print(s1 - s2)  # print(s1.difference(s2))
print(s1 ^ s2)  # print(s1.symmetric_difference(s2))

print(s1.isdisjoint(s2))  # True if not common elements in both sets

s1.clear()  # object is not deleted in clear method
del s2  # completely deleted

print(s1)
