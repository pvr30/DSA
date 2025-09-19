class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    cur = head
    while cur:
        print(cur.data, end="->")
        cur = cur.next
    print()

def removeDuplicates(head):
    cur = head
    while cur and cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(30)
head.next.next.next.next = Node(30)


printList(head)
removeDuplicates(head)
print('After remove duplicates..')
printList(head)

