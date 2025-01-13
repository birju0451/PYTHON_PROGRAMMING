class Rectangle:
    def set_dimension(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):##this is methode or function which is call by object patamweter
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
#create an object        
rectangle1=Rectangle()
rectangle1.set_dimension(4,5)
print("the length and breadth is:",rectangle1.length,rectangle1.breadth)
print("the area is :",rectangle1.area())
print("the perimeter is :",rectangle1.perimeter())