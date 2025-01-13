class Rectangle:
    def __init__(self,length,breadth):
        print(f"a rectangle is created with length :{ length} and breadth:{breadth}")
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
#create an object        
rectangle1=Rectangle(4,5)
rectangle2=Rectangle(40,50)
# rectangle1.set_dimension(4,5)
print("the length and breadth is:",rectangle1.length,rectangle1.breadth)
print("the area is :",rectangle1.area())
print("the perimeter is :",rectangle1.perimeter())

print("the length and breadth is:",rectangle2.length,rectangle2.breadth)
print("the area is :",rectangle2.area())
print("the perimeter is :",rectangle2.perimeter())