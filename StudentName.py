class StudentName:
    def __init__(self, name, marks):
        self.__name = name
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            self.__marks = 0
            print("Error: Invalid marks")

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getMarks(self):
        return self.__marks

    def setMarks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Error: Invalid marks")


c = StudentName("alice", 100)
c.setMarks(95)
c.setName("Alice")
print(c.getName())
print(c.getMarks())