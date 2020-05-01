class Student:
    college = 'UCLA'
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print('Student Name: ',self.name)
        print('Student Roll No: ', self.roll)
        print('Student Marks: ', self.marks)
        print('College: ',Student.college)
        section = 'A'
        print('Section: ', section)
        print()

S = Student('aaa',101,78.25)
S.display()
Student.section = 'B'
S.display()




