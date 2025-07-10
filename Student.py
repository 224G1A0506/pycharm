class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)
s1=Student(name='jhon',age=30)
print(s1.name)
print(s1.age) 
    