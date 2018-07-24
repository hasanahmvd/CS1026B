from random import randint
list1 = []

for i in range(20):
    num = randint(0,99)
    list1.append(num)

print(list1)
list1.sort()
print(list1)
