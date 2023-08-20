class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enque(self, item):
        self.items.insert(0, item)

    def size(self):
        return len(self.items)

    def deque(self):
        return self.items.pop()


q = Queue()

print(q.isEmpty())
q.enque(2)
for i in q.items:
    print(i, end=" ")
print()
q.enque("hello")
for i in q.items:
    print(i, end=" ")
print()
q.enque(5.4)
for i in q.items:
    print(i, end=" ")
print()
print(q.size())
print(q.deque())
for i in q.items:
    print(i, end=" ")

print(q.isEmpty())
