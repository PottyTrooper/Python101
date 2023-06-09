testString = "You Cant Have Cereal Without Cereal"

# for loop with range() function
for i in range(0, len(testString), 1):
    print(testString[i], end="🤔 ")

print("\r")

# for each loop in python
# eachChar represents the character in the current iteration
# as we iterate through the string
for eachChar in testString:
    print(eachChar, end="😩 ")

print("\r")

# Question 1 - Print every character in the testString except for letter "O" "o"
#               USING THE FOR-EACH LOOP APPROACH AND CONTINUE STATEMENT
def removeO():
    for i in range(0, len(testString), 1):
        if testString[i] == "o" or "O":
            print("", end="")
        else:
            print(testString[i], end="")

# Question 2 - To count the occurances of letter "O" "o" in the testString
# Use for-each loop, declare a new variable "count" to keep the count
# declare new variable and geclare it as "count"
# create a for-each loop to loop through test string
# in the loop check if the character in the current itteration (eachChar)
# is it a letter "o" or "O"

Count = 0
for eachChar in testString:
    if eachChar == "o" or "O":
        Count += 1

print(Count)

# Question 3 - To print every character before the second letter "O" or "o"
# Cut off at the second letter "O" or "o"
# for each loop, break, count variable
count = 0
for eachChar in testString:
    if eachChar == "O" or eachChar == "o":
        count += 1

    if count > 1:
        break


    print(eachChar, end=" ")