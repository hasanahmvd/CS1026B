# Replace the placeholders and run the Python program

import random
name = (raw_input("Please enter your name: "))

for x in range(1, 21):
    print("test",x)
    if x % 3 == 0:
        print(name)
    if x % 2 == 0:
        print(random.randint(1,10))
