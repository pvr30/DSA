# Open Addressing

class MyHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.BUCKET = [-1] * self.capacity

    def hash(self, x):
        return x % self.capacity

    def insert(self, element):
        index = self.hash(element)
        for i in range(index, self.capacity):
            if self.BUCKET[i] in (-1, -2):
                self.BUCKET[i] = element
                return True
        return False

    def search(self, element):
        index = self.hash(element)
        for i in range(index, self.capacity):
            if self.BUCKET[i] == element:
                return True
        return False

    def delete(self, element):
        index = self.hash(element)
        for i in range(index, self.capacity-1):
            if self.BUCKET[i] == element:
                self.BUCKET[i] = -2
                break

    def get_table(self):
        return self.BUCKET


h = MyHash(7)
h.insert(2)
h.insert(49)
h.insert(56)
h.insert(21)
h.insert(50)

print(h.search(21))

h.delete(56)

print(h.search(56))

print(h.get_table())

h.insert(22)
h.insert(69)
h.insert(68)


print(h.get_table())
