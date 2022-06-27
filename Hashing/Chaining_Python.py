# Chaining

class MyHash:
    def __init__(self, b):
        self.BUCKET = b
        self.table = [[] for _ in range(b)]

    def insert(self, x):
        i = x % self.BUCKET
        self.table[i].append(x)

    def remove(self, x):
        i = x % self.BUCKET
        try:
            self.table[i].remove(x)
        except:
            pass

    def search(self, x):
        i = x % self.BUCKET
        return x in self.table[i]

    def getTable(self):
        return self.table


h = MyHash(7)

h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(12)

print(h.search(56))

h.remove(56)

print(h.search(56))

print(h.getTable())

