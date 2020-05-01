class A():
    def displayA(self):
        print('Display Method of Class A')

class B(A):
    def displayB(self):
        print('Display Method of Class B')

class C(A):
    def displayC(self):
        print('Display Method of Class C')

b = B()
b.displayA()
b.displayB()

c = C()
c.displayA()
c.displayC()
#c.displayB() #Do with or without


