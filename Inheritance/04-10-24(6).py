'''2.Problem Statement: Create a base class Vehicle with attributes brand and model. 
Then, create two derived classes Car and Bike, both inheriting from Vehicle,
 and adding their own attributes and methods.

Tasks:
Define a base class Vehicle with attributes brand and model.
Create a derived class Car that inherits from Vehicle and adds an attribute num_doors.
Create another derived class Bike that inherits from Vehicle and adds an attribute type.
Implement methods to display the details of the vehicles.
Create instances of both Car and Bike and display their information.'''

class vehicle :
    def __init__(self, Brand,Model):
        self.Brand = Brand
        self.Model = Model
    def display_info(self):
        print(f"Brand:{self.Brand}")
        print(f"Model :{self.Model}")

class Car (vehicle):
    def __init__(self, Brand, Model,num_doors):
        super().__init__(Brand,Model)
        self.num_doors = num_doors
    def display_info(self):
        super().display_info()
        print(f"Number of doors :{self.num_doors}")

class Bike (vehicle):
    def __init__(self, Brand, Model,type):
        super().__init__(Brand, Model)
        self.type =type
    def display_info(self):
        super().display_info()
        print(f"Type : {self.type}")

Car = Car("KIA",2024,4)
Bike = Bike("Royal Enfield",2023,"ABS")

print("Car details:") 
Car.display_info()

print("Bike Details:")
Bike.display_info()