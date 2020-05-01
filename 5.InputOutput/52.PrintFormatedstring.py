x = 10
y = 20
z = 30

# %X is format specifiers
print('Value: %i' %x) #signed decimal value
print('Value: %i' %y)
print('Value: %d' %x) #signed decimal value
print('Value: %d' %y)
print('Value: %f' %y) #float value
print('Value: %f' %x)
print('Value: %s' %y) #String, can also be used for List, set, tuple check
print('Value: %s' %x)

print('Value of x=%d, y=%d, z=%d' %(x,y,z))

name = 'abc'
marks = [78.25, 89.46, 64.95]
print('Student Name: %s has marks: %s' %(name,marks))

rating = 4.24812
print('Rating: {}'.format(rating))
print('Rating: %f' %rating)
print('Rating: %.2f' %rating)

