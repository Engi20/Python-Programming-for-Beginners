class Student:
    def __init__(self):
        self.name = ''
        self.roll = 0
        self.marks = 0

    def getStudentData(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def displayS(self):
        print('Student Name: ',self.name)
        print('Roll No: ', self.roll)
        print('Marks: ', self.marks)

class Placements(Student):
    def __init__(self):
        self.company = ''
        self.package = ''

    def getPlacementData(self,company,package):
        self.company = company
        self.package = package

    def displayP(self):
        print('Company: ',self.company)
        print('Package: ', self.package)

P = Placements()
P.getStudentData('abc',101,78.25)
P.getPlacementData('Dell',48000)
P.displayS()
P.displayP()




