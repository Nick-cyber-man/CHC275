list.__getitem__
dict.__getitem__
class Person:
    def___init___(self,name,ssn,address,num):
        self.name = name
        self.___ssn= ssn
        aelf.address = address
        self.phone = num
        
    def greetings(self):
        print(f"Hello, I am {self.name}, my address is {self.address}, and my phone number is {self.phone}")
Persona = Person("john", "nick", "alex")
persona.greetings()

class Student(Person):
    def ___init___(self,name,ssn,address,num,school):
        super().__init__(self,name,ssn,address,num)
        self.school = school
    def greeting(self):
        pass
    studentA = Student("micheal","222222")
    studentA.greetings()
    
    
class SpecialNumber():
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        