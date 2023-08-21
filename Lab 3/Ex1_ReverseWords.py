# Reverse each word in a string using a Stack
# Words must stay in the same initial position
# E.g., "Algorithm and Data Structures" will become "mhtiroglA dna ataD serutcurtS"

from LinearDataStructures.stack import Stack

# Reverse each words of a string maintaining their position
def reverserWords(input_string):
    st = Stack()
    revString = ""
    words = input_string.split()

    for word in words:
        for c in word:
            st.push(c)

        while not st.isEmpty():
            revString = revString + st.pop()
        revString += " "

    # return the reversed string
    return revString


# Test Code
if __name__ == "__main__":
    myString = "Algorithm and Data Structures"
    print(reverserWords(myString))