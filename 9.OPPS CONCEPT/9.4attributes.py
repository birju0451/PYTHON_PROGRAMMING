class Student:
    def set_details(self, name, roll):
        self.name = name#class attributes
        self.roll = roll

    def get_name(self):
        return self.name
    
    def get_roll(self):
        return self.roll

# Creating instances of the Student class
student1 = Student()
student1.suare_area=1000 #object attibutes
student1.set_details("Birju", 216)  # Pass both name and roll
print(f"Name: {student1.get_name()}, Roll: {student1.get_roll()}")
print(student1.suare_area)

student2 = Student()
student2.set_details("Manish", 217)  # Pass both name and roll
print(f"Name: {student2.get_name()}, Roll: {student2.get_roll()}")
