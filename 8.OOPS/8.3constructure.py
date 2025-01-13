class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    # def set_dimension(self,length,breadth):
    #     self.length=length
    #     self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
#create an object
length=int(input("enter length")) 
breadth=int(input("enter width"))       
rectangle1=Rectangle(length,breadth)
# rectangle1.set_dimension(4,5)
print("the length and breadth is:",rectangle1.length,rectangle1.breadth)
print("the area is :",rectangle1.area())
print("the perimeter is :",rectangle1.perimeter())

length=int(input("enter length")) 
breadth=int(input("enter width"))       
rectangle2=Rectangle(length,breadth)
# rectangle1.set_dimension(4,5)
print("the length and breadth is:",rectangle2.length,rectangle2.breadth)
print("the area is :",rectangle2.area())
print("the perimeter is :",rectangle2.perimeter())