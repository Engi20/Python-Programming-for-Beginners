class A():
    def displayA(self):
        print('Display Method of Class A')

class B(A):
    def displayB(self):
        print('Display Method of Class B')

b = B()
b.displayA()
b.displayB()

class C(B):
    def displayC(self):
        print('Display Method of Class C')

c = C()
c.displayA()
c.displayB()
c.displayC()


