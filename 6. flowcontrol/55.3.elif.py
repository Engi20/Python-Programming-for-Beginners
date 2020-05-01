n = int(input('Enter Age: '))

print('Age Classification')
if n > 0 and n <= 12:
    print('Your Age is :', n)
    print('You are a Kid')
elif n > 12 and n <= 19:
    print('Your age is :', n)
    print('You are a Teenager')
elif n > 19 and n <= 40:
    print('Your age is :', n)
    print('You are Young')
elif n > 40 and n <= 60:
    print('Your age is :', n)
    print('You are becomming old')
elif n > 60 and n <= 100:
    print('Your age is :', n)
    print('Its old age')
else:
    print('Invalid age')
    
print('End of Program')
