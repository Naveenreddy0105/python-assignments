'''2.Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
  Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
  Exercise:
   >Create multiple employee instances.
   >Print the total number of employees after adding each new employee.
   >Check whether changing the total_employees in one instance affects the others.'''


class Company:
    total_employees=0 
    #Static variable to track total employees
    def __init__(self,name,department):
        self.name=name
        self.department=department
        Company.total_employees +=1 
    #Increment total_employees on each new employee
    def display_info(self):
        print("Name:",{self.name})
        print("Department:",{self.department})
    @classmethod
    def get_total_employees(cls):
        return cls.total_employees
# Create multiple employee instances
emp1=Company("Naveen","software")
print("Total Employees:",Company.get_total_employees())
emp2=Company("lohi","analyst")
print("Total Employees:",Company.get_total_employees())
emp3=Company("eswar","SQL")
print("Total Employees:",Company.get_total_employees())
# Check if changing total_employees in one instance affects other
emp1.total_employees=100 
#Attempts to change total_employees
print("Emp1 Total Employees:",emp1.total_employees)
print("Emp2 Total Employees:",Company.get_total_employees())
#Display employee information
print("Employee Information:")
emp1.display_info()
print()
emp2.display_info()
print()
emp3.display_info()