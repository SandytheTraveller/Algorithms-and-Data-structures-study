class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

# insert element on "front"
    def addFront(self, item):
        self.items.append(item)

# insert an element on "rear"
    def addRear(self, item):
        self.items.insert(0, item)

# remove and return a current element on "front"
    def removeFront(self):
        return self.items.pop()

    # remove and return a current element on "rear"
    def removeRear(self):
        return self.items.pop(0)

d = Deque()
print(d.isEmpty())
d.addRear(2)
for i in d.items:
    print(i, end=" ")
print()
d.addRear("hello")
for i in d.items:
    print(i, end=" ")
print()
d.addFront(5.4)
for i in d.items:
    print(i, end=" ")
print()
print(d.size())
d.removeFront()
for i in d.items:
    print(i, end=" ")
print()
d.removeRear()
for i in d.items:
    print(i, end=" ")
print()