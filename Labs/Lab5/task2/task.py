# Replace the placeholders and complete the Python program.

def factorial(n):
    result = n
    for i in range(n-1,1,-1):
        result = result * i
    return result

print(factorial(5))
print(factorial(7))
print(factorial(9))
