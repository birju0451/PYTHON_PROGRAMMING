# ord() function
# ord() returns the Unicode (ASCII) value of a character

char = 'a'
print("Character:", char, "-> ASCII value:", ord(char))  # a = 97

char = ' '   # space character
print("Character: space -> ASCII value:", ord(char))     # space = 32

char = '0'
print("Character:", char, "-> ASCII value:", ord(char))  # 0 = 48

char = '9'
print("Character:", char, "-> ASCII value:", ord(char))  # 9 = 57

char = 'z'
print("Character:", char, "-> ASCII value:", ord(char))  # z = 122


# chr() function
# chr() returns the character of a given ASCII value

number = 65
print("ASCII value:", number, "-> Character:", chr(number))  # 65 = A
