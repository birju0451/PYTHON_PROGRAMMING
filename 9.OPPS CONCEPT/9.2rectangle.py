class Rrectangle:

    def set_dimension(self,height,width):
        self.h=height
        self.w=width

    def area(self):
        return self.h*self.w
    
    def perimeter(self):
        return 2*(self.h+self.w)
    
#create an object 
rectangle1=Rrectangle()
rectangle1.set_dimension(7,5)
print(f"area is:{rectangle1.area()},perimeter{rectangle1.perimeter()}")