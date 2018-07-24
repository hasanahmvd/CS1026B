# Replace the placeholders and complete the Python program.

def isMultiple(n):
    if n % 7 == 0:
        return n
    else:
        return -1


def checkMultiples():
    for i in range(1, 100):
        cur = isMultiple(i)
        if cur != -1:
            print(cur)


# Run the test
checkMultiples()
