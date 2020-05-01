class Student:
    '''This is version 1.0'''

    def __init__(self):
        self.name = 'abc'
        self.roll = 101
        self.marks = 78.25

    def __str__(self):
        return 'This is Student Class'

    def display(self):
        print('Student Name: ',self.name)
        print('Student Roll No: ', self.roll)
        print('Student Marks: ', self.marks)
        print()

S = Student()
print(S)
print(S.__doc__)
print(S.name)
print(S.roll)
print(S.marks)
S.display()


