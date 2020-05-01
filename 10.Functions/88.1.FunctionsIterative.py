def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

num = input('Enter Number: ')
n = int(num)
f = factorial(n)
print('Factorial(',n,'): ',f)
