import random

# N = int(input("Enter N: "))
# R = int(input("Enter R: "))

N = 100
R = 100

# receives in input two numbers (N, R) and returns a list of N integer
# numbers with random values from 0 to R
def createRandomList(N, R):
    l = []
    for i in range(N):
        l.append(random.randint(0, R))
    return l

# given a list of numbers returns
# how many even and odd numbers contains
def countEvenOdd(l):
    evens = 0
    odds = 0
    for i in l:
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds

# given a list of numbers returns two lists, one containing the even numbers
# and the other the odd numbers
def splitEvenOdd(l):
    evens = []
    odds = []

    for i in l:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return evens, odds

_list = createRandomList(N, R)
evenNums, oddNums = countEvenOdd(_list)
evens, odds = splitEvenOdd(_list)

print("number of even numbers: ", evenNums)
print("number of odd numbers: ", oddNums)

print("even numbers: ", evens)
print("odd numbers: ", odds)
