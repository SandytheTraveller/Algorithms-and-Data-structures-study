# DIFFICULT: Check whether or not a valid expression has redundant parentheses

from LinearDataStructures.stack import Stack


# Function to check redundant parentheses in a valid expression
# It returns True is there are duplicate parentheses False otherwise
def checkRedundancy(expression):

    # set of valid operators
    operators = {"+", "-", "/", "*"}

    # create an empty stack
    st = Stack()

    # iteration through the whole expression
    for elem in expression:
        # if the current elemet is a closing parenthesis ")"
        if elem == ')':
            top_elem = st.pop()
            # set a flag redundant for True
            isRedundant = True
            # pop the top element of the stack until an opening paranthesis "("
            while top_elem != '(':
                # check if the top element is an operator
                if top_elem in operators:
                    isRedundant = False
                top_elem = st.pop()
            # if no operator is present, then the parentheses are redundant
            if isRedundant:
                return True

        else:
            st.push(elem) # push open parenthesis '(', operators and operands to stack

    return False


# Function that prints the result
def isRedundant(expression):
    if checkRedundancy(expression) is True:
        print("The expression has redundant parentheses")
    else:
        print("The expression has no redundant parentheses")


# Test code
if __name__ == '__main__':
    exp = "( (a + b) )"  # Redundant
    isRedundant(exp)

    exp = "( a + (b) / c )"  # Redundant
    isRedundant(exp)

    exp = "( a + ( (b + c) ) )"  # Redundant
    isRedundant(exp)

    exp = "(a + b * (c - d) )"  # Not redundant
    isRedundant(exp)
