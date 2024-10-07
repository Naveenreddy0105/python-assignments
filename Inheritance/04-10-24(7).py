'''5. Hybrid Inheritance
Problem Statement: Create a class structure to represent hybrid inheritance:

Device: Base class with name attribute.
Phone: Derived from Device with an additional phone_number attribute.
Tablet: Derived from Device with an additional screen_size attribute.
Smartphone: Derived from both Phone and Tablet with an additional attribute os.

Tasks:
Define a base class Device with an attribute name.
Define a class Phone that inherits from Device and adds an attribute phone_number.
Define a class Tablet that inherits from Device and adds an attribute screen_size.
Define a class Smartphone that inherits from both Phone and Tablet, adding an attribute os.
Implement methods to display all attributes of the Smartphone.
Create an instance of Smartphone and display its information.'''


class Device :
    def __init__(self,name):
        self.name = name
    def display_info(self):
        print(f"Device Name:{self.name}")

class Phone (Device) :
    def __init__(self,name,phone_number):
        super().__init__(name,phone_number)
        self.phone_number = phone_number
    def display_info(self):
        super().display_info()
        print(f"Phone Number :{self.phone_number}")

class Tablet(Device):
    def __init__(self, name,screen_size):
        super().__init__(name)
        self.screen_size= screen_size
    def display_info(self):
        super().display_info()
        print(f"screen size :{self.screen_size}")

class Smartphone (Phone,Tablet):
    def __init__(self, name, phone_number,screen_size,os):
        Phone.__init__(self,name,phone_number)
        Tablet.__init__(self,name,screen_size)
        self.os = os
    def display_info(self):
        Phone.display_info(self)
        print(f"operating system:{self.os}")

smartphone = Smartphone ("Iphone16",7890233454,"6.5 inches","ios")
print("Smartphone Details:")
smartphone.display_info()