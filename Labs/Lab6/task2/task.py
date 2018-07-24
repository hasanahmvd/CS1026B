# Replace the placeholders and complete the Python program.

def someSame(one, two) :
    for a in one :
        for b in two :
            if a == b :
                return True
    return False

# Define some lists of numbers
someNumbers = [1,2,3,4,5,6,7,8,9,0]
someOtherNumbers = [11,22,33,44,55,66,77,88,99,100]

# See if these two lists have one element the same
print(someSame(someNumbers,someOtherNumbers))

# Define another list
someMoreNumbers = [111,222,333,444,555,6,777,888,999,1000]
# Check the new list and one of the others
print(someSame(someNumbers,someMoreNumbers))

