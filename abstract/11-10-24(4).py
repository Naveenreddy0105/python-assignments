'''4.Create a base class Employee with attributes name and salary, and methods get_details() and get_salary().
 Then create two subclasses:

Manager, which adds an attribute department.
Developer, which adds an attribute programming_language.
Both subclasses should override the get_details() method to include their respective
 additional attributes in the returned string.
'''
class Employee :
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
    def get_details(self):
        f"Name: {self.name}" 
        f"salary :{self.salary}"
    def get_salary (self):
        return self.salary

class Manager (Employee) :
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    def get_details(self):
        f"Name :{self.name}"
        f"salary :{self.salary}"
        f"department : {self.department}"

class Developer (Employee):
    def __init__(self, name, salary,programing_langauage):
        super().__init__(name, salary)
        self.programing_language = programing_langauage

def get_details(self):
    f"name :{self.name}"
    f"salary :{self.salary}"
    f"progarming_language :{self.programing_language}"

manager = Manager("Naveen",50000,"HR") 
developer = Developer("Navya",90000,"python")

print(manager.get_details())
print(developer.get_details())

Manager.increase_salary(10)
developer.increase_salary(15)

print(Manager.get_details())
print(developer.get_details())