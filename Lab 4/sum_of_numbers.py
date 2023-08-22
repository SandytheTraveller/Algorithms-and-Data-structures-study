# recursive solution
def list_sum(numList):
    if len(numList) == 0:
        return 0
    else:
        return numList[0] + list_sum(numList[1:])


print(list_sum([1, 3, 5, 7, 9]))

def list_sum_it(numList):
    sum = 0
    for i in numList:
        sum += i
    return sum

