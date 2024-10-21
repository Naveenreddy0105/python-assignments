class P:
    def __init__(self):
        print("this is parent class contsructor")
 
    def m1(self):
        print("this is parent class  instance")
 
    @classmethod
    def m2(self):
        print("this is parent class  classmethod")
 
    @staticmethod
    def m3():
        print("this is parent class  staticmethod")
 
class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
   
    def display(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
   
   
    @staticmethod
    def m4():
        #super().m1()
        super(C,C).m3()       #only way top access parent class static method from child class static method
        #super().m2()
        #super().m3()
 
    @classmethod
    def m5(cls):
        super(C,cls).__init__(cls)   #access parent class constructor
        super(C,cls).m1(cls)         #acces parent class instnace
        #super().m1()
 
c = C()
c.display()
print("------------------")
c.m4()
 
print("---------------")
c.m5()
 
class person:
    def __init__(self,name, age):
        self.name = name
        self.age  = age
 
    def m1(self):
        print(self.name)
        print(self.age)
 
class employee(person):
    def __init__(self,name,age, id, salary ):
        super().__init__(name, age)
        self.id = id
        self.salary  = salary
 
    def m1(self):
        super().m1()
        print(self.id)
        print(self.salary)
 
 
e1 = employee("ram",30,1001, 50000)
e1.m1()