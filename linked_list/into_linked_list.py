"""
A linked list is a linear data structure where elements (nodes) are linked together
sequentially through pointers or references, allowing dynamic memory allocation.
Each node contains data and a reference to the next node in the sequence.
Unlike arrays, linked lists do not require contiguous memory allocation
"""

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)

temp1.next = temp2
temp2.next = temp3

head = temp1
print(head.key)
print(head.next.key)
print(head.next.next.key)

# Another method to make linked list
temp1 = Node(100)
temp1.next = Node(200)
temp1.next.next = Node(300)
