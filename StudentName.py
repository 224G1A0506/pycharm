class StudentName:
    def __init__(self,name,marks):
        self.__name=""
        self.__marks=0
    def getName(self):
        return self.__name
    def setName(self):
        self.__name = name 
    def getMarks(self):
        return self.__marks
    def setMarks(self):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("error")
    def getMarks(self):
        return self.__marks

c=StudentName("alice",100)
c.setMarks()
c.setName("Alice")
print(c.getName())
print(c.getMarks())