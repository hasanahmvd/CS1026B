# Replace the placeholders and complete the Python program.

def lenWords(words):
    result = []
    for i in words:
        result.append(len(i))
    return result

# Define a list of words
words = ["hello","good","nice","as","at","baseball","absorb","sword","a","tall","so","bored","silver","hi"
,"pool","we","I","am","seven","Do","you","want","ants","because","that's","how","you","get"]

# Print the list of the lengths of the words
print(lenWords(words))

