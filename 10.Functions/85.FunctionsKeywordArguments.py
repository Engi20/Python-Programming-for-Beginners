def myfunction(x, y, z):
    print('Value x:',x)
    print('Value y:',y)
    print('Value z:',z)
    w = x + y + z
    print('Value w:',w)

myfunction(3,5,8)
myfunction(z=3,x=5,y=8)
myfunction(3,z=5,y=8)
myfunction(3,x=5,y=8)

