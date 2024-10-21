'''1.Create a class Vehicle with attributes brand and year. The class should have a method get_info() 
that returns the brand and year of the vehicle.
Then, create two subclasses:

Car, which adds an attribute number_of_doors.
Motorcycle, which adds an attribute has_sidecar.
Both subclasses should override the get_info() method to include their respective additional attributes in the returned string.'''

class Vehicle :
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def get_info(self):
        print(f"brand :{self.brand}")
        print(f"year : {self.year}")

class Car (Vehicle) :
    def __init__(self, brand, year,num_of_doors):
        super().__init__(brand, year)
        self.num_of_doors = num_of_doors
    def get_info(self):
        print(f"brand : {self.brand}")
        print(f"year  :{self.year}")
        print(f"num_of_doors :{self.num_of_doors}")

class Motorcycle (Vehicle):
    def __init__(self, brand, year,has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar =has_sidecar
    def get_info(self) :
        sidecar_info ="yes" if self.has_sidecar else "No"
        print (f"brand : {self.brand}")
        print(f"year : {self.year}")
        print(f"has_sidecar :{self.sidecar_info}")

car = Car("KIA",2022,4)
motorcycle = Motorcycle("royal enfield",2024,True) 

print(car.get_info())
print(motorcycle.get_info())
