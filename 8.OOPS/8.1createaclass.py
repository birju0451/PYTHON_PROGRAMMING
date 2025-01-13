class student:
    def set_name(self,name):
        self.name=name##name ko access kiye hai ya chalu kiye hai
    def get_name(self):
        return self.name
student1=student()
student1.set_name('birju')

print(student1.get_name())