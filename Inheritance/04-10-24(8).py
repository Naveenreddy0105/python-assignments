'''6.Basic Inheritance
Problem Statement: Create a class Person with attributes: name and age. 
Create another class Student that inherits from Person and has an additional attribute grade.
Define methods in both classes to display the attributes.

Tasks:
Define a Person class with an __init__ method to initialize name and age.
Define a Student class that inherits from Person, with an additional attribute grade.
Define a display_info method in both Person and Student classes to print all attributes.
Create objects for both Person and Student and display their information.'''

class Person :
    def __init__(self,name,age) :
        self.name =name
        self.age = age
    def display_info(self) :
        print(f"Name :{self.name},age :{self.age}")

class Student (Person):
    def __init__(self,name,grade):
        super().__init__(name,grade)
        self.grade = grade
    def display_info(self):
        
        print(f"grade :{self.grade}")

Person = Person ("Naveen",26)
student=Student("naveen","O")
print("Person details :")
Person.display_info()
print("Student details :")
student.display_info()