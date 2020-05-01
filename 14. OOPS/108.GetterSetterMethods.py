class Student:

    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name

    def setRoll(self,roll):
        self.roll = roll
    def getRoll(self):
        return self.roll

    def setMarks(self,marks):
        self.marks = marks
    def getMarks(self):
        return self.marks

    def display(self):
        print('Student Name: ',self.name)
        print('Roll No: ', self.roll)
        print('Marks: ',self.marks)

S = Student()
S.setName('abc')
S.setRoll(101)
S.setMarks(78.56)
S.display()
