class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print('Student Name: ',self.name)
        print('Student Roll No: ', self.roll)
        print('Student Marks: ', self.marks)
        print()

    def profile(self):
        self.city = 'London'


S = Student('aaa',101,78.25)
print(S.__dict__)
S.marks = 46.25
print(S.__dict__)
S.grade ='A'
print(S.__dict__)
S.profile()
print(S.__dict__)
del S.marks
print(S.__dict__)



