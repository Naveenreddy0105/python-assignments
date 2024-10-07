'''2.Problem Statement: Create two base classes: Bird and Flyable. 
Bird should have an attribute species, and Flyable should have a method fly(). 
Then, create a derived class Eagle that inherits from both Bird and Flyable.

Tasks:
Define a class Bird with an attribute species.
Define a class Flyable with a method fly() that prints "Flying".
Create a class Eagle that inherits from both Bird and Flyable, and has a method to display species and flying capability.
Create an instance of Eagle and call its methods.'''

class Bird :
    def __init__(self,species) :
        self.species = species

class Flyable :
    def fly (self) :
        print("flying")

class Eagle (Bird,Flyable) :
    def __init__(self, species):
        Bird.__init__(self,species)

    def display_BF(self):
        print(f"species : {self.species}")
        self.fly()

Eagle = Eagle("Golden Eagle")
Eagle.display_BF()



