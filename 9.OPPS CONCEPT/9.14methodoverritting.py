class animal:
    def speak(self):
        pass

class dog(animal):
    def speak(self):
      print("bark")
    
class cow(animal):
    def speak(self):
       print(super().speak())    

#object of class 
d=dog()

d.speak()
