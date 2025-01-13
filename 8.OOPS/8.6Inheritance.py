class parent():
    def __init__(self):
        print("this is parent class")
        self.super_atributes=True
class child(parent):
    def __init__(self):
        super().__init__()
        print("thish is child class")

child1=child()

