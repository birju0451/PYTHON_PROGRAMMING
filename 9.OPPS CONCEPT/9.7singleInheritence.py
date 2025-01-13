#create class and sub class 
class vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity=seating_capacity

    def get_fare(self):
        return self.seating_capacity*100
    
class bus(vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def get_fare(self):
        vehicle_fare= super().get_fare()
        maintanance_fare=0.1*vehicle_fare
        total_fare=vehicle_fare+maintanance_fare
        return total_fare
    
#create object 
vehicle1=vehicle(50)
print("total fare is:",vehicle1.get_fare())

bus1=bus(50)
print("total bus fare is:",bus1.get_fare())