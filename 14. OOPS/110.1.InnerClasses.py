class College:
    def __init__(self):
        print('College Outer Class Constructor')

    class Student:
        def __init__(self):
            print('Student Inner Class Constructor')

        def displayS(self):
            print('Student Class Method')

    def displayC(self):
        print('College Class Method')

C = College()
S = C.Student()
S.displayS()
C.displayC()
#S.displayC()
#C.displayS()
print()
S1 = College().Student()
S1.displayS()


