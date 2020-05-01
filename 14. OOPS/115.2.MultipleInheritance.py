class A():
    def display(self):
        print('Display Method of Class A')

class B():
    def display(self):
        print('Display Method of Class B')

class C(A,B):
    def displayC(self):
        print('Display Method of Class C')

class D(B,A):
    def displayD(self):
        print('Display Method of Class C')

c = C()
c.display()
c.displayC()
print()
d = D()
d.display()
d.displayD()



