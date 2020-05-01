class Student:
    def __init__(self):
        self.name = ''
        self.roll = 0
        self.marks = 0
        print('Student Constructor')

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
        #super().__init__() #Do without & with
        self.company = ''
        self.package = ''
        print('Placement Constructor')

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




