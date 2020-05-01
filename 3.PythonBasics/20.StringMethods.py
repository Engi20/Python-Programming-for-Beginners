my_str='This is Python'

x = my_str.count('s')
print(x)
x = my_str.count('p')
print(x)
x = my_str.count('t')
print(x)
x = my_str.count('is')
print(x)

print()
x = my_str.index('s')
print(x)
x = my_str.index('t')
print(x)
x = my_str.index('is')
print(x)
#x = my_str.index('p')
print(x)

print()
x = my_str.find('s')
print(x)
x = my_str.find('t')
print(x)
x = my_str.find('is')
print(x)
x = my_str.find('p')
print(x)

my_str=' This is Python   '
x = my_str.strip()
print(x)
x = my_str.strip(' Tn')
print(x)
x = my_str.strip(' To')
print(x)

my_str='This is Python'
x = my_str.split()
print(x)
x = my_str.split('P')
print(x)
x = my_str.split('is')
print(x)

my_str='10 20 30 40 50'
x = my_str.split()
print(x)

my_str='10,20,30,40,50'
x = my_str.split(',')
print(x)

my_str='This is Python'
x = my_str.replace('h','z')
print(x)
x = my_str.replace('is','z')
print(x)
x = my_str.replace('z','a')
print(x)

my_str='This is Python'
x = my_str.upper()
print(x)
x = my_str.lower()
print(x)

my_str='This is Python'
x = my_str.islower()
print(x)
x = my_str.isupper()
print(x)
x = my_str.isalpha()
print(x)
x = my_str.isdigit()
print(x)


