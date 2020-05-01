class College:
    def __init__(self,name,roll,marks):
        self.s = self.Student(name,roll,marks)

    class Student:
        def __init__(self,name,roll,marks):
            self.name = name
            self.roll = roll
            self.marks = marks

        def displayS(self):
            print('Student Name: ',self.name)
            print('Roll: ', self.roll)
            print('Marks: ', self.marks)
            print()

    def change(self):
        self.s.marks = self.s.marks + 5

    def displayC(self):
        self.s.displayS()

C = College('abc',101,78.25)
C.displayC()
C.change()
C.displayC()




