x = 10
y = 20
print( x is y )
print( x is not y )
x = 10
y = 10
print( x is y )
print( x is not y )
print()

x = 10.25
y = 20.50
print( x is y )
print( x is not y )
x = 10.25
y = 10.25
print( x is y )
print( x is not y )
print()

x = True
y = False
print( x is y )
print( x is not y )
x = False
y = False
print( x is y )
print( x is not y )
print()

x = 'Hello'
y = 'Python'
print( x is y )
print( x is not y )
x = 'Hello'
y = 'Hello'
print( x is y )
print( x is not y )
x = 'Hello'
y = 'hello'
print( x is y )
print( x is not y )
print()

print()
#Check where to demonstrate in which lecture
l1 = [10,20,30]
l2 = [10,20,30]
print(id(l1))
print(id(l2))
print( l1 is l2 )
print( l1 == l2 )

l3 = l1
print( l1 is l3 )
print( l1 == l3 )
print(id(l1))
print(id(l2))
print(id(l3))




