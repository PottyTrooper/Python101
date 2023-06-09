# String Duplication
print("+" + "-" * 50 + "+")
for i in range(5):
    print("|" + " " * 50 + "|")
print("+" + "-" * 50 + "+")

def ProcessAString():
    # srting test thingy
    str1 = input("enter whatever you want to say: ")
    for i in range(0, len(str1), 1):
        print(str1[i], end="---")

def ReverseAString():
    # reverse a string
    str1 = input("enter whatever you want to say backwards: ")
    for i in range((len(str1) - 1), -1, -1):
        print(str1[i], end="")

ReverseAString()

