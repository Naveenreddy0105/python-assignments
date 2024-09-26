'''1.Create a class Person that has instance variables name, age, and gender. Add methods to:
Initialize these variables.
Update the age.
Display the person's information.
 Exercise:
 > Create multiple instances of the Person class.
 > Change the age of one person and display the updated information.'''

'''
class person :
    def __init__ (self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def update_age(self,new_age):
        self.age = new_age

    def display_info(self):
        print("person name :",self.name)
        print("person age :",self.age)
        print("person gender: ",self.gender)

person1 =person ("naveen",26,"male")
person2 = person("praveen",29,"male")
person3 =person ("rajesh",45,"male")
person4 =person("harika",23,"female")
person5 =person ("anusha",22,"female")

person1.display_info()
person2.display_info()
person3.display_info()
person4.display_info()
person5.display_info()

person3.update_age(25)
print("age_updating")
person3.display_info()
'''

class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def update_age(self,age_new):
        self.age=age_new

    def display_info(self):
        print(f"Name - {self.name},age - {self.age},gender - {self.gender}")

person1 =person ("ram",23,"male")
person2 =person ("sita",21,"female")
person3 =person ("laxman",26,"male")

person1.display_info()
person2.display_info()
person3.display_info()

print("updating age")

person1.update_age(29)
print("age updating")
person1.display_info()





