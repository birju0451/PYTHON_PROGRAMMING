class Rrectangle:

    def __init__(self,height,width):
        self.h=height
        self.w=width

    def area(self):
        return self.h*self.w
    
    def perimeter(self):
        return 2*(self.h+self.w)
    
#create an object 
rectangle1=Rrectangle(7,6)
print(f"area is:{rectangle1.area()},perimeter{rectangle1.perimeter()}")
rectangle2=Rrectangle(10,10)
print(f"area is:{rectangle2.area()},perimeter{rectangle2.perimeter()}")
rectangle3=Rrectangle(10,20)
print(f"area is:{rectangle3.area()},perimeter{rectangle3.perimeter()}")

