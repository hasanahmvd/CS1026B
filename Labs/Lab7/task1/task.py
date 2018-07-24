from __future__ import print_function

# Replace the placeholders and run the Python program.

text = open("text.txt","r")
for line in text:
    print(line,end = "")
text.close()

