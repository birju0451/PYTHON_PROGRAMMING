"""
File Name: python_datatypes_and_print_notes.py

Topic:
- Basic Python Data Types
- print() function
- Variable update
- Separator (sep)
"""

# -------------------------------
# STRING (str)
# -------------------------------
# A string is a sequence of characters written inside quotes.

name = "birju"
print(type(name))      # <class 'str'>


# -------------------------------
# INTEGER (int)
# -------------------------------
# Integer represents whole numbers (no decimal point).

roll_number = 216
print(type(roll_number))   # <class 'int'>


# -------------------------------
# FLOAT (float)
# -------------------------------
# Float represents decimal numbers.

percentage = 82.5
print(type(percentage))    # <class 'float'>


# -------------------------------
# BOOLEAN (bool)
# -------------------------------
# Boolean has only two values: True or False.

is_student = True
print(type(is_student))    # <class 'bool'>


# -------------------------------
# PRINTING MULTIPLE VALUES
# -------------------------------
# print() can display multiple values separated by spaces.

print(name, roll_number, percentage, is_student)


# -------------------------------
# STRING CONCATENATION
# -------------------------------
# Strings can be joined using + operator.
# Numbers should be printed using comma (,).

print("My name is " + name + " and roll number is", roll_number)


# -------------------------------
# PRINTING TEXT WITH NUMBERS
# -------------------------------
# Comma allows mixing strings and numbers safely.

print("I scored", percentage, "% in my final exam. I am a student.")


# -------------------------------
# UPDATING A VARIABLE
# -------------------------------
# Variable values can be changed during program execution.

percentage = 94.5
print(name, percentage)


# -------------------------------
# PRINTING EXPRESSIONS
# -------------------------------
# Python evaluates expressions inside print().

print("My percentage has changed to", percentage + 1)


# -------------------------------
# USING SEPARATOR (sep)
# -------------------------------
# sep changes the default space between printed values.

print(name, roll_number, percentage, is_student, sep="-")


# -------------------------------
# CUSTOM SEPARATOR EXAMPLE
# -------------------------------

x = 1
y = 2
z = 3
print(x, y, z, sep="->")
