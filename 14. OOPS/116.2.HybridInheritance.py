class A():
    def displayA(self):
        print('Display Method of Class A')

class B(A):
    def display(self):
        print('Display Method of Class B')

class C(A):
    def display(self):
        print('Display Method of Class C')

class D(B,C): #B,C and then C,B
    def displayD(self):
        print('Display Method of Class D')

b = B()
b.displayA()
b.display()
print()
c = C()
c.displayA()
c.display()
print()
d = D()
d.displayA()
d.display()
d.displayD()



