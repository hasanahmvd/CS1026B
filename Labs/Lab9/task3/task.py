# Replace the placeholders with code and run the Python program

sentence ="I had such a horrible day. It was awful, so bad, sigh. It could not have been worse but actually though "\
          +"such a terrible horrible awful bad day."

makeItHappy ={"horrible":"amazing","bad":"good","awful":"awesome","worse":"better","terrible":"great"}

spsentence = sentence.split()
for word in range(0,len(spsentence)):
    if spsentence[word] in makeItHappy:
        spsentence[word] = makeItHappy[spsentence[word]]

newString=""

#for word in spsentence:
#    newString = newString + word + " "

newString = '\n'.join(spsentence)

print(newString)

