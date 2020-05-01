class A():
    def display(self):
        print('Class A Method')

class B:
    def display(self):
        print('Class B Method')

class Demo(A,B):
    def displayD(self):
        print('Class C Method')

d = Demo()
d.display()
print(Demo.mro())
