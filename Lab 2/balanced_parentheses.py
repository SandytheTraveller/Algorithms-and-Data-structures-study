# check if a string contains a balanced number of parentheses
from stack import Stack

openers = ["(", "[", "{"]
closers = [")", "]", "}"]

# the match is done comparing the indexes of the two lists
# corresponding to the current open and close elements
def matches(open, close):
    return openers.index(open) == closers.index(close)
def parentheses_checker(symbols_string):
    s = Stack()

    for symbol in symbols_string:
        # if the current symbol is an opening parenthesis,
        # it is pushed in the stack
        if symbol in openers:
            s.push(symbol)
        else:
            if s.isEmpty():
                return False
            else:
                # if the current symbol is a closing parenthesis, check if the element
                # on top of the stack is an opening of the correct type
                if symbol in closers:
                    top = s.pop()
                    if not matches(top, symbol):
                        return False
    if s.isEmpty():
        return True

t = "( [ ] { } )"
print(parentheses_checker(t))
