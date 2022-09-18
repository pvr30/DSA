# Traverse Through the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


def printLList(head):
    cur = head
    while cur:
        print(cur.data, end="->")
        cur = cur.next
    print()


# search for an element in a linkedlist

def search(head, x):
    cur = head
    pos = 1
    while cur:
        if cur.data == x:
            return pos
        pos += 1
        cur = cur.next
    return -1


if __name__ == '__main__':
    printLList(node1)
    print()

    print(search(node1, 20))
    print(search(node1, 2))
