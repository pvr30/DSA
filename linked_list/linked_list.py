class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

    # Traverse in a list
    def printList(self):
        cur = self
        while cur != None:
            print(cur.data, end="->")
            cur = cur.next
        print()

    # Search in a list
    def search(self, x):
        cur = self
        pos = 1
        while cur:
            if cur.data == x:
                return pos
            cur = cur.next
            pos += 1
        return -1

# insert at begin
def insertBegin(head, x):
    temp = Node(x)
    temp.next = head
    return temp

# insert at end
def insertEnd(head, x):
    if head is None:
        return Node(x)
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = Node(x)
    return head

# insert at given position
def insertPos(head, x, pos):
    temp = Node(x)
    if pos == 1:
        temp.next = head
        return temp

    cur = head
    for i in range(pos-2):
        cur = cur.next
        if cur is None:
            return head

    temp.next = cur.next
    cur.next = temp
    return head

def delFirst(head):
    if head is None:
        return None
    else:
        return head.next

def delEnd(head):
    if head is None:
        return None
    if head.next is None:
        return None
    cur = head
    while cur.next.next is not None:
        cur = cur.next
    cur.next = None
    return head

def delNode(ptr):
    temp = ptr.next
    ptr.data = temp.data
    ptr.next = temp.next

def sortedInsert(head, x):
    temp = Node(x)
    if head is None:
        return temp
    elif x < head.data:
        temp.next = head
        return temp
    else:
        cur = head
        while cur.next is not None and x > cur.next.data:
            cur = cur.next
        temp.next = cur.next
        cur.next = temp
        return head

def printMiddleMethod1(head):
    if head is None:
        return
    count = 0
    cur = head
    while cur:
        cur = cur.next
        count += 1

    cur = head
    for i in range(count // 2):
        cur = cur.next
    print(cur.data)

def printMiddleMethod2(head):
    if head is None:
        return
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    print(slow.data)

def printNthFromEndMethod1(head, n):
    len = 0
    cur = head
    while cur:
        cur = cur.next
        len += 1
    cur = head
    for i in range(1, len-n+1):
        cur = cur.next
    print(cur.data)

def printNthFromEndMethod2(head, n):
    if head is None:
        return
    first = head
    for i in range(n):
        if first is None:
            return
        first = first.next

    second = head
    while first:
        second = second.next
        first = first.next

    print(second.data)

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

head.printList()
print(head.search(30))
print(head.search(50))

head = None
head = insertBegin(head, 10)
head = insertBegin(head, 20)
head = insertBegin(head, 30)

head.printList()

head = None
head = insertEnd(head, 10)
head = insertEnd(head, 20)
head = insertEnd(head, 30)

head.printList()

head = insertPos(head, 15, 2)
head = insertPos(head, 25, 4)
head.printList()

# head = delFirst(head)
# delNode(head)
# head = delFirst(head)
#
# head.printList()
#
# head = delEnd(head)

# head.printList()

head = sortedInsert(head, 7)
head = sortedInsert(head, 17)
head.printList()

printMiddleMethod1(head)
printMiddleMethod2(head)

printNthFromEndMethod1(head, 3)
printNthFromEndMethod2(head, 3)
