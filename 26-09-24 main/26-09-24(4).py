'''4.Create a class Employee where:
  Each employee has an instance variable salary.
  There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
  Write a method total_salary that calculates the total salary for an employee (including the bonus).
  Exercise:
   >Create several employee instances with different salaries.
   >Change the bonus amount (static variable) and see how it affects all employees.
   >Calculate and print the total salary for each employe'''

class Employee:
    bonus=0.1 
    #  bonus(10%)
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def total_salary(self):
        return self.salary+(self.salary*Employee.bonus) 

#create employee instance salaries
emp1=Employee("Naveen",80000)
emp2=Employee("lohi",60000)
emp3=Employee("eswar",70000)

print("Initial Total Salaries:")
print(f"{emp1.name}:${emp1.total_salary():.2f}")
print(f"{emp2.name}:${emp2.total_salary():.2f}")
print(f"{emp3.name}:${emp3.total_salary():.2f}")
Employee.bonus=0.15
 
print("\nUpdate Total Salaries(15% bonus):")
print(f"{emp1.name}:${emp1.total_salary():.2f}")
print(f"{emp2.name}:${emp2.total_salary():.2f}")
print(f"{emp3.name}:${emp3.total_salary():.2f}")