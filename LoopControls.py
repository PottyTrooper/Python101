# for loop
# it is used when we specificaly know the number of repetitions
for i in range(0, 5, 1):
    print("😩")

# while loop
# It is used when we're certain about the number of repetitions
# But we know the condition for which the loop has to remain active
# loop manipulation techniques
# 1. To alter the execution speed/frequency of a loop
# 2. Break - Terminate the loop immediately
# 3. continue - The continue statement exits the current iteration
#               and starts a new iteration immediately!


import time

gay_count = 0
while gay_count < 100:
    gay_count = gay_count + 1
    print("🟥" + "-" + str(gay_count))
    time.sleep(0.1)
    print("🟧")
    time.sleep(0.1)
    print("🟨")
    time.sleep(0.1)
    print("🟩")
    time.sleep(0.1)
    print("🟦")
    time.sleep(0.1)
    print("🟪")
    time.sleep(0.1)

    if gay_count < 50:
        continue

    print("wow u patient")
    time.sleep(1)


print("im tired of printing 🤕")