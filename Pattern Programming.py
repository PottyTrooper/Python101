import time

randomV = 2
def waaave():
    while True:
        for i in range(5):
            print("🤔" * randomV)
            randomV = randomV + 2
            time.sleep(0.05)
        for i in range(5):
            print("🤔" * randomV)
            randomV = randomV -2
            time.sleep(0.05)

"""
e.g. rowNum = 5
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
randomV2 = 1
for i in range(5):
    print((str(randomV2) + " ") * randomV2)
    randomV2 = randomV2 + 1
    time.sleep(0.05)

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
for verydumb in range(2, rowNum + 1)
for dumb in range(1, verydumb, 1):
        print(dumb, end=" ")

    print("\r")

