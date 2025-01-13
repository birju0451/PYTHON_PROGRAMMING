#attributes
class student:
    def set_name(self,name):
        self.name=name##class atributes
    def get_name(self):
        return self.name
student1=student()
student1.set_name('birju')
print(student1.get_name())
student1.english_marks=30##instance attributes
print(student1.english_marks)