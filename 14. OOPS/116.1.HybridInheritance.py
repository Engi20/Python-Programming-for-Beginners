class A():
    def displayA(self):
        print('Display Method of Class A')

class B(A):
    def displayB(self):
        print('Display Method of Class B')

class C(A):
    def displayC(self):
        print('Display Method of Class C')

class D(B,C):
    def displayD(self):
        print('Display Method of Class D')

b = B()
b.displayA()
b.displayB()
print()
c = C()
c.displayA()
c.displayC()
print()
d = D()
d.displayA()
d.displayB()
d.displayC()
d.displayD()



