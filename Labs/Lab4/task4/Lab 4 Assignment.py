num = int(input("How many numbers do you want to use today? "))
x = 1
value = int(input("Enter the number: "))
max = value
min = value
total = value

while x < num:
    value = int(input("Enter the number: "))
    if value > max:
        max = value
    if value < min:
        min = value

    total = total + value
    x = x + 1
avg = total / x
range = max - min

print("The average of the values is "+str(avg))
print("The smallest of the values is "+str(min))
print("The largest of the values is "+str(max))
print("The range of the values is "+str(range))
