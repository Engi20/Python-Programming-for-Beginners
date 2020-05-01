class A():
    def displayA(self):
        print('Display Method of Class A')

class B():
    def displayB(self):
        print('Display Method of Class B')

class C(A,B):
    def displayC(self):
        print('Display Method of Class C')

c = C()
c.displayA()
c.displayB()
c.displayC()



