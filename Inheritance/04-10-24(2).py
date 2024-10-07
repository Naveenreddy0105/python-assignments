'''2. Multiple Inheritance

1.Problem Statement: Create a class Teacher with an attribute subject.
 Then, create a class Researcher with an attribute field.
Finally, create a class TeachingResearcher that inherits from both Teacher and Researcher,
 and has an additional method to display both attributes.

Tasks:
Define a Teacher class with an __init__ method to initialize subject.
Define a Researcher class with an __init__ method to initialize field.
Define a TeachingResearcher class that inherits from both Teacher and Researcher, and has an __init__ method to initialize both subject and field. Add a method to display both.
Create an object of TeachingResearcher and display its attributes.'''

class Teacher :
    def __init__ (self,subject):
        self.subject = subject

class Researcher :
    def __init__(self,field) :
        self.field = field

class TeachingResearcher(Teacher,Researcher):
    def __init__(self, subject, field):

        Teacher.__init__(self,subject)
        Researcher.__init__(self,field)

    def display_attributes (self):
        print(f"subject : {self.subject}")
        print(f"Field  :{self.field}")

TR = TeachingResearcher(subject="Maths",field="python")
TR.display_attributes()

