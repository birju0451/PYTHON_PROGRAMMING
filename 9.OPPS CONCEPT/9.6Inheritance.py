class parent:
    def __init__(self):
        print("this is parent class")
        self.super_attributes=True
        
class child(parent):

    def __init__(self):
        super().__init__()
        print("this is child class")
        print(self.super_attributes)

#object for child class 
child1=child()