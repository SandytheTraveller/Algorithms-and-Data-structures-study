class Stack:
    def __init__(self):
        self.items = []

    # check if the stack is empty
    def isEmpty(self):
        return self.items == []

    # insert an element
    def push(self, item):
        self.items.append(item)

    # remove and return the last element
    def pop(self):
        return self.items.pop()

    # return the last element, but do not remove it
    def peak(self):
        if len(self.items) > 0:
            return self.items[-1]

    def size(self):
        return len(self.items)
