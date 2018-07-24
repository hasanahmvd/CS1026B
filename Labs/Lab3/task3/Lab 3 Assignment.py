x = (input("Please enter your first number: "))
y = (input("Please enter your second number: "))
z = (input("Please enter your third number: "))

if x > y and y > z :
    print("descending")
elif x < y and y < z :
    print("ascending")
else :
    print("not in order")
