# Second Exercise: Delete the middle element of Stack
#
# Write a script to remove the middle element of a Stack
# E.g.: input [1, 2, 3, 4, 5]
#       output [1, 2, 4, 5]
#
# NOTE: you can solve the problem using an auxiliary stack or using recursion


from LinearDataStructures.stack import Stack

# iterative solution with auxiliary Stack
def deleteMidElem(st):
    num_el = st.size() // 2 # 4
    new_s = Stack()

    while num_el != 0:
        new_s.push(st.pop())
        num_el -= 1

    st.pop()

    while not new_s.isEmpty():
        st.push(new_s.pop())

    return st



# Test Code
if __name__ == "__main__":
    st = Stack()

    for i in range(1, 10):
        st.push(i)

    print(st.items)
    deleteMidElem(st)
    print(st.items)
