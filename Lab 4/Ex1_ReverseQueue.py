# Reverse the content of a Queue using Recursion
# You can use only one Queue, no other data structures are needed
# You cannot use any iterative loop
from LinearDataStructures.queue import Queue

# [9, 8, 7, 6, 5, 4, 3, 2, 1] # start
# [1, 2, 3, 4, 5, 6, 7, 8, 9] # result

def reverseQueue(q):
    if q.size() == 0:
        return

    elem = q.deque()
    reverseQueue(q)
    q.enqueue(elem)


if __name__ == "__main__":
    q = Queue()

    for i in range(1, 10):
        q.enqueue(i)

    print(q.items)
    reverseQueue(q)
    print(q.items)
