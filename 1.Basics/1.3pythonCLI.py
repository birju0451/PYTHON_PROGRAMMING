# This is a single-line comment
# Python program to understand basics

print("Program Started")
print("Hello World")

# Using new line
print("Under\nStand")

"""
This is a multi-line comment.
It is used to write long explanations.
"""

# Indentation example with if
if 5 > 2:
    print("5 is greater than 2")
    print("These lines are inside if block")

print("This line is outside if block")

# Loop with indentation
for i in range(3):
    print("Loop number:", i)
    print("This line is inside loop")

print("Loop ended")

# Function using def
def greet(name):
    print("Hello", name)
    print("Welcome to Python")

# Calling function
greet("Birju")

# Another function
def add(a, b):
    return a + b

result = add(10, 20)
print("Addition result:", result)

print("Program Finished")
