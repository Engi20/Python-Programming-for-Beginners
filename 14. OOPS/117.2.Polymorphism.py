class A():
    def display(self):
        print('Class A Method')

class B(A):
    def display(self):
        print('Class B Method')

b = B()
b.display()
