x = eval('10')
print(type(x))
x = eval('10.75')
print(type(x))
x = eval('True')
print(type(x))

#x = eval('Hello') #Not Possible
#print(type(x))


#x = input('Enter Value: ')
#print(type(x))

#y = eval(input('Enter Value: '))
#print(type(y))
#print(y)

#we alreay have several type casting functions such as int(x), float(x), bool(x)
#The eval() provides the flexibility of implicitly converting the value to its respective type
#Instead of using different type casting functions we can use eval()
#eval() also evaluates expressions eval(x+y)
#input
#10
#10.75
#True
#10+2.5
#10+2.5+True
