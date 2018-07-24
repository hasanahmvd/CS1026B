# Fix the print statement in the following Python program and then run it.

# Note how to get input from the keyboard
celsius = float(input("Please enter the Celsius value: "))
# Notice how we had to cast celsius to float try removing the float cast and see what happens.
# When you take a value from input it is a string value by default.
# Therefore you must convert it to whatever other type of value if you to.
# In this case we convert it to a "float" value.

# Note 1.8 is 9/5
# fDegrees stores the Fahrenheit value
fDegrees = (celsius * 1.8 )+ 32
print("The degrees in Fahrenehit is {}".format(fDegrees))


