import time

snailList = ["snail", "wet snail"]

snailList.insert(1, "fast snail")

# print(snailList)

dumbNumList = []
for i in range(10):
    dumbNumList.append(i)
    print(dumbNumList)

dumbNumList2 = []
for i in range(1, 11, 1):
    dumbNumList2.insert(0, i)
    print(dumbNumList2)

"""
dumbNumList3 = [1, 2, 3]
del dumbNumList3[-1]
print(dumbNumList3)
"""

dumbNumList4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in range(len(dumbNumList4)):
    del dumbNumList4[-1]
    print(dumbNumList4)

while True:
    dumbNumList2 = []
    for i in range(1, 11, 1):
        dumbNumList2.insert(0, i)
        time.sleep(0.1)
        print(dumbNumList2)

    dumbNumList4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(len(dumbNumList4)):
        del dumbNumList4[-1]
        time.sleep(0.1)
        print(dumbNumList4)
