def countVowels(string):
    noVowels = 0
    for char in string:
        if char in "aeiouAEIOU":
            noVowels = noVowels + 1
    return noVowels

returnVal = countVowels("foiae")
print(returnVal)
