'''4. Multilevel Inheritance
Problem Statement: Create a class hierarchy where Person is the base class, Employee is derived from Person, 
and Manager is derived from Employee. Each class should add an additional attribute,
 and a method to display all attributes from the hierarchy.

Tasks:
Define a base class Person with attributes name and age.
Define a derived class Employee with an additional attribute salary.
Define another derived class Manager that inherits from Employee and adds an attribute department.
Implement methods to display the information in each class.
Create an instance of Manager and display its information.'''

class person :
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def display_peron_info (self):
        print(f"name:{self.name},age : {self.age}")

class employee :
    def __init__(self,name,age,salary): 
        person.__init__(self,name,age)
        self.salary = salary
    def display_employee_info(self) :
        self.display_employee_info()
        print(f"salary: {self.salary}")

class manager (employee):
    def __init__(self,name,age,salary,department):
        employee.__init__(self,name,age,salary)
        self.department =department
    def display_manager_info(self):
        print(f"department:{self.department}")
        print(self.name)
        print(self.age)
        print(self.salary)

manager = manager ("Naveen",26,60000,"Developer")
manager.display_manager_info()
