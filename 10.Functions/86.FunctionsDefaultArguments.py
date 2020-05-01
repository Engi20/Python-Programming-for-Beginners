def myfunction(x, y=4, z=7):
    print('Value x:',x)
    print('Value y:',y)
    print('Value z:',z)
    w = x + y + z
    print('Value w:',w)

myfunction(3,5,8)
myfunction(3,5)
myfunction(3)
myfunction()