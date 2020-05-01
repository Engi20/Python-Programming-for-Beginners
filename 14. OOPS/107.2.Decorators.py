class Demo:
    z = 30
    @classmethod #show with and without
    def add(cls,x,y):
        print('Sum:',x+y+cls.z)

S = Demo()
S.add(10,20)
Demo.add(10,20)
