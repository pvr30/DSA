
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

# or

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)