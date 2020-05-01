class Student:
    def __init__(self):
        self.name = 'abc'
        self.roll = 101
        self.marks = 78.25
        print('In Constructor')

    def display(self):
        print('Student Name: ',self.name)
        print('Student Roll No: ', self.roll)
        print('Student Marks: ', self.marks)
        print()

S = Student()
S.__init__()


