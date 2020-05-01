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
        #print('Department: ',Student.dept)
        Student.section = 'A'
        print('Section: ', Student.section)
        print()

S = Student('aaa',101,78.25)
#S.display()
Student.dept = 'CSE'
S.display()




