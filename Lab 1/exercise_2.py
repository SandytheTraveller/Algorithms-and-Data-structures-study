# reads a text file and memorizes all the lines in a list
def readTxtFile(filename):
    fin = open(filename)
    l = []
    for line in fin:
        words = line.split(' ')
        for i in words:
            l.append(i)

    return l

# capitalizes the first letter of each word in each line and save the result in a new list
def capitalizeWords(l):
    newList = []
    for i in l:
        if i[0].islower():
            newList.append(i[0].upper() + i[1:])
        else:
            newList.append(i)
    return newList

# writes the capitalized text in a new text file
def writeTxtFile(l):
    savename = "loremipsum_cap.txt"
    fout = open(savename, 'w')
    for i in l:
        fout.write(i + ' ')


filename = 'loremipsum.txt'
_list = readTxtFile(filename)
print(_list)
capitalized = capitalizeWords(_list)
print(capitalized)
writeTxtFile(capitalized)