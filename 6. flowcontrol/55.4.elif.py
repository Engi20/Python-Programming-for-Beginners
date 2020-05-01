n = int(input('Enter Age: '))

print('Age Classification')
if 0 < n <= 12:
    print('Your Age is :', n)
    print('You are a Kid')
elif 12 < n <= 19:
    print('Your age is :', n)
    print('You are a Teenager')
elif 19 < n <= 40:
    print('Your age is :', n)
    print('You are Young')
elif 40 < n <= 60:
    print('Your age is :', n)
    print('You are becomming old')
elif 60 < n <= 100:
    print('Your age is :', n)
    print('Its old age')
else:
    print('Invalid age')

print('End of Program')
