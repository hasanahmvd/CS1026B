# Replace the placeholders and complete the Python program.

def zFirst(words):
    # We will need two lists
    zresult =[]
    result =[]
    for word in words:
        if word.lower()[0] == 'z':
            # If it does, add it to the first list
            zresult.append(word)
        else:
            # Does not begin with a 'z'
            result.append(word)

    zresult.sort()
    result.sort()
    return zresult + result

# Define a list of words
words=["hello","good","nice","as","at","baseball","absorb","sword","a","tall","so","bored","silver",
       "hi","pool","we","am","seven","do","you","want","ants","because","that's","how","you","get",
       "zebra","zealot","zoo","xylophone","asparagus"]

# Print the result of using zFirst
print(zFirst(words))

