# Third Exercise
#
# Reversing the content of Stack using recursion
# You can use only one Stack, no other data structures are needed
# You cannot use any iterative loop
#
# HINT: you need TWO recursive functions one to empty the stack one to fill in


from LinearDataStructures.stack import Stack

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [9, 8, 7, 6, 5, 4, 3, 2, 1]

def reverseStack(st):
    if st.isEmpty():
        return

    elem = st.pop()
    reverseStack(st)
    fill_stack(st, elem)

def fill_stack(st, item):
    if st.isEmpty():
        st.push(item)

    else:
        t = st.pop()
        fill_stack(st, item)
        st.push(t)

if __name__ == "__main__":
    st = Stack()

    for i in range(1, 10):
        st.push(i)

    print(st.items)
    reverseStack(st)
    print(st.items)
