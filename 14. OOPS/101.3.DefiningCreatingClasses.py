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

Students = [ Student('aaa',101,78.25),
      Student('bbb',102,62.75),
      Student('ccc',103,89.50)]

for s in Students:
    s.display()
