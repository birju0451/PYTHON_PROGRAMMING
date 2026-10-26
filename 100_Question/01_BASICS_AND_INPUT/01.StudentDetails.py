name = input("Enter your name :")
age = int(input("Enter your valid age:"))
cgpa = float(input("Enter you current cgpa :"))

print("Student Details :")
# print("name :" + name +"\nage :", age ,"\nCGPA :", cgpa)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa:.3f}")
