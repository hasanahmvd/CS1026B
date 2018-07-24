list1 = []

while len(list1)<10:
    v = int(input("Enter a number: "))
    if v not in list1:
        list1.append(v)

print(list1)
