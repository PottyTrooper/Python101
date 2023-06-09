"""
Write a Python program to add 'ing' at the end
of a given string (length should be at least 3).
If the given string already ends with 'ing',
add 'ly' instead. If the string length of the given
string is less than 3, leave it unchanged.
"""

# examples
# work - working
# doing - doingly
# oh - oh

#a parameterised function(a function that accepts inputs
def addToString(testString):
    if len(testString) > 2:
        # process information
        if testString[-3::1] == "ing":
            print (testString + "ly")
        else:
            print (testString + "ing")

    else:
        print(testString)


# addToString("Ohio")
# addToString("Is")
# addToString("Not")
# addToString("Dangerous")

# Question 2
# Given any String of odd length greater than 7,
# print out the middle 3 characters line by line
# testString = "SwissCottage1"
# Output: C
#         o
#         t

def mid3(testString):
    if len(testString) % 2 == 1 and len(testString) > 7:
        middleIndex = int((len(testString) - 1) / 2)
        print(testString[middleIndex - 1]) # mid left
        print(testString[middleIndex]) # mid
        print(testString[middleIndex + 1]) # mid right

mid3("396069278")

# Question 3
# remove the n-th index character from a nonempty string
# a parameterised function with two parameters
def remove_char(teststring, n):
    first_part = teststring[0:n:1]
    second_part = teststring[n + 1::1]
    print(first_part + second_part)

remove_char("PooPooPeePee", 5)

# Write a Python program to change a given
# string to a new string where the first and last chars
# have been exchanged.
teststring = "hamborgor"
print ((teststring[-1])+(teststring[1:-1:1])+(teststring[0]))

# Question 5
# prints all odd charaters in any string using a for loop
def filter_odds(testString):
    for i in range(1, len(testString), 2):
        print(testString[i])

def filter_evens(testString):
    for i in range(0, len(testString), 2):
        print(testString[i])

filter_odds("HAMBORGOR")
filter_odds("YUMMY")
