'''1. Single Inheritance
Problem Statement: Create a base class Animal with an attribute name and a method speak().
 Then, create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".

Tasks:
Define a base class Animal with an __init__ method that takes name as a parameter.
Define a method speak() in Animal that prints "Animal sound".
Create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".
Create an instance of Dog and call the speak() method.'''

class Animal:
        def __init__(self,name) :
              self.name = name
        
        def speak (self):
            print("Animal sound")

class Dog(Animal):
      def speak(self):
            print("Bark")

Dog = Dog("Buddy")
Dog.speak()

  