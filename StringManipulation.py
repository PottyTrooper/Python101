# string slicing
TestString = "Timothy"

# subtrat - imo
print(TestString[1:4:1])

# given any string that has at least 7 characters
# extrant and join the first and last three characters of the string
# sample
# "HONGJIANG"
# "HONANG"
# solve this problem
while True:
    ToContinue = input("would you like to continue? (Y/N)")
    if ToContinue == "Y":
        TestString2 = input("type your sentence with less than 7 characters: ")
        if len(TestString2) >= 7:
            print((TestString2[:3:1]) + (TestString2[len(TestString2)-3::1]))
        else:
            print("that aint gonna work >:(")

    elif ToContinue == "N":
        print("bye have a great time")
        break

    else:
        print("only leters are accepted dude")
