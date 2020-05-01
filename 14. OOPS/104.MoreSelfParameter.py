class Student:
    def __init__(a,name,roll,marks):
        a.name = name
        a.roll = roll
        a.marks = marks

    def display(self):
        print('Student Name: ',self.name)
        print('Student Roll No: ', self.roll)
        print('Student Marks: ', self.marks)
        print()

S = Student('aaa',101,78.25)
S.display()

