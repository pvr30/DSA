l = [10, 20, 45, 60, 12]

print(l[:]) # [10, 20, 45, 60, 12]
print(l[1:]) # [20, 45, 60, 12]
print(l[2:4]) # [45, 60]

print(l[1:4:2]) # [20, 60]
print(l[-1:-4:-1]) # [12, 60, 45]

print(l[::-1])  # [12, 60, 45, 20, 10]


l1 = [1, 2, 3, 4, 5]
l2 = l1[:]  # this give another list
print(l1 is l2) # False

t1 = (1, 2, 3, 4)
t2 = t1[:]
print(t1 is t2)  # True

s1 = "vishal"
s2 = s1[:]
print(s1 is s2)  # True

