'''2.Define an abstract class Animal with an abstract method make_sound().
 Then, create three classes that inherit from Animal:

Dog with the sound "Woof".
Cat with the sound "Meow".
Cow with the sound "Moo".
Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method.'''

from abc import ABC, abstractmethod
 
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
 
class Dog(Animal):
    def make_sound(self):
        return "Woof"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow"
 
class Cow(Animal):
    def make_sound(self):
        return "Moo"
 

def play_sound(animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()
cow = Cow()
 
play_sound(dog)  
play_sound(cat)  
play_sound(cow)  