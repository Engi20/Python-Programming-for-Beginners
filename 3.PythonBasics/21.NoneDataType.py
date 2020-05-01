x = 10
print(x)
print(type(x))

x = None
print(x)
print(type(x))

x = 10
y = print(x)
print(x)
print(y)
print(id(x))
print(id(y))

y = print('Hello')
w,x,z = None, None, None
print(id(w))
print(id(x))
print(id(y))
print(id(z))

