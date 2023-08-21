from deque import Deque

def palchecker(aString):
    charDeque = Deque()

    for ch in aString:
        charDeque.addRear(ch)

    while charDeque.size() > 1:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            return False

    return True
