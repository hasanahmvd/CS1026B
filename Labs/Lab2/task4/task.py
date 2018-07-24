# Try the following Python code and answer the questions

# Lets try some simple formatting
name= "Sterling Archer"
age = 36

# Two ways of formatting strings
# The first is called interpolation in this case %s represents a string and is the first element
# %d represents an integer and is the second element in the list
print("%s %d" % (name, age))

# The second method calls a format function.
# It replaces the {} with the variables in the format function in order.
print("{}{}".format(name,age))

# Print the following string and integer variables using the interpolation method
course = "CS1026a"
year = 2016
print("%s %d" % (course, year))

print("{} {}".format(course,year))


