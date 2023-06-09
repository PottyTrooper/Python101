superDumbNumList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
otherDumbNumList = []
def Odd_Number_Filter(HEHEHEHAA):
    for eachNum in HEHEHEHAA:
        if eachNum % 2 == 1:
            otherDumbNumList.append(eachNum)

# Odd_Number_Filter([*range(1,101, 1)])


print(otherDumbNumList)

def max_thingy(aPrettyDumbList):
    currentMax = aPrettyDumbList[0]
    for eachNum in aPrettyDumbList:
        if eachNum > currentMax:
            currentMax = eachNum
    return currentMax

# print(max_thingy([1,2,3,4,5,6,7,8,9,10]))

def not_max_thingy(aReasonablyDumbList):
    currentNotMax = aReasonablyDumbList[0]
    for eachNum in aReasonablyDumbList:
        if eachNum < currentNotMax:
            currentNotMax = eachNum
    return currentNotMax

# print(not_max_thingy([10,9,8,7,6,5,4,3,2,1]))

def dumb_addition(aPoliticalyDumbList):
    the_addition_thingy = 0
    for eachNum in aPoliticalyDumbList:
        the_addition_thingy = the_addition_thingy + eachNum
    return the_addition_thingy

# print(dumb_addition([33,12,6,6,6,3,3]))

def dumb_addition(aPoliticalyDumbList):
    the_addition_thingy = 0
    for eachNum in aPoliticalyDumbList:
        the_addition_thingy = the_addition_thingy + eachNum
    return the_addition_thingy

print(dumb_addition([33,12,6,6,6,3,3]))
