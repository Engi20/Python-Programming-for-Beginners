class Student:
    def __init__(self):
        self.name = 'abc'
        self.roll = 101
        self.marks = 78.25
    def displayS(self):
        print('Student Name: ',self.name)
        print('Roll No: ', self.roll)
        print('Marks: ', self.marks)

class Placements:
    def __init__(self):
        self.s = Student()
    def displayP(self):
        print('Student Name: ',self.s.name)
        print('Roll No: ', self.s.roll)
        print('Marks: ', self.s.marks)

P = Placements()
P.displayP()


