# Insert and Delete Operation on a linkedlist

from Traversing_Search_Linkedlist import printLList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Insertion Operations


def insertBegin(head, data):
    temp = Node(data)
    temp.next = head
    return temp


def insertEnd(head, data):
    if head is None:
        return Node(data)
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = Node(data)
    return head


def insertPosition(head, data, index):
    temp = Node(data)
    if index == 1:
        temp.next = head
        return temp
    cur = head
    for i in range(index - 2):
        cur = cur.next
        if cur is None:
            return head
    temp.next = cur.next
    cur.next = temp
    return head


# Delete Operations
def deleteBegin(head):
    if head is None:
        return None
    else:
        return head.next


def deleteEnd(head):
    if head is None:
        return None
    if head.next is None:
        return None
    cur = head
    while cur.next.next:
        cur = cur.next
    cur.next = None
    return head


def deleteIndex(head, index):
    if head is None:
        return None
    if index == 1:
        head = deleteBegin(head)
        return head
    cur = head
    for _ in range(index - 2):
        cur = cur.next
        if cur.next is None:
            return head

    if cur.next.next is None:
        head = deleteEnd(head)
        return head

    cur.next = cur.next.next
    return head


def sortedInsertion(head, val):
    temp = Node(val)
    if head is None:
        return temp
    elif val < head.data:
        temp.next = head
        return temp
    else:
        cur = head
        while cur.next and cur.next.data < val:
            cur = cur.next
        temp.next = cur.next
        cur.next = temp
        return head

if __name__ == '__main__':
    head = None
    head = insertBegin(head, 30)
    head = insertBegin(head, 20)
    head = insertBegin(head, 10)
    printLList(head)

    head = insertEnd(head, 40)
    head = insertEnd(head, 50)
    printLList(head)

    head = insertPosition(head, 25, 1)
    head = insertPosition(head, 35, 5)
    head = insertPosition(head, 55, 8)
    head = insertPosition(head, 100, 10)
    printLList(head)

    head = deleteBegin(head)
    head = deleteBegin(head)

    printLList(head)

    head = deleteEnd(head)
    head = deleteEnd(head)
    printLList(head)

    head = deleteIndex(head, 2)
    printLList(head)

    head = sortedInsertion(head, 45)
    head = sortedInsertion(head, 10)
    head = sortedInsertion(head, 25)

    printLList(head)
