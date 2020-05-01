class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def displayS(self):
        print('Student Name: ',self.name)
        print('Roll No: ', self.roll)
        print('Marks: ', self.marks)

class Placements:
    def __init__(self,company,package,stud):
        self.company = company
        self.package = package
        self.stud = stud
    def displayP(self):
        self.stud.displayS()
        print('Company: ',self.company)
        print('Package: ', self.package)

S = Student('abc',101,78.25)
P = Placements('Dell',48000,S)
P.displayP()


