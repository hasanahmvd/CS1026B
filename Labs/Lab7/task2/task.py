# Replace the placeholders and complete the program.

text = open("text.txt","r")
myfile =open("myfile.txt","w")
line = text.readline()
words = line.split()
for word in words:
    print(word)
    myfile.write(word)

# Close the files
text.close()
myfile.close()
