class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print('Student Name: ',self.name)
        print('Roll No: ', self.roll)
        print('Marks: ', self.marks)
        print()

class StudentReports:
    def change(stud): #stud is not self variable, This method is treated as static method
        stud.marks = stud.marks + 5
        stud.display()

S = Student('abc',101,78.25)
S.display()
StudentReports.change(S)
S.display() # Execute without and then with this statement


