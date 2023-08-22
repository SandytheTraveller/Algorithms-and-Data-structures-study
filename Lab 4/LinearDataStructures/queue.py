class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, item):
        self.items.insert(0, item)

    def size(self):
        return len(self.items)

    def deque(self):
        return self.items.pop()

