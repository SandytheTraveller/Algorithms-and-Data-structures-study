class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peak(self):
        if not self.isEmpty():
            return self.peak()

    def size(self):
        return len(self.items)


text = input()
words = text.split()
for word in words:
    s = Stack()

    for c in word:
        s.push(c)

    while not s.isEmpty():
        print(s.pop(), end="")

