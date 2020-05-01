#In command run as python test.py 10 20 30

from sys import argv
#sys built-in Module contains argv
#argv is a variable

print(type(argv)) #Type is List

print(argv)
print(len(argv))

for x in range(1,len(argv)):
    print(argv[x])
    print(type(eval(argv[x])))
    print(type(argv[x]))

#Application Sum of any Number of operands through command line arguments
sum = 0
for x in range(1,len(argv)):
    sum += eval(argv[x])
print(sum)

sum=0
mycomdlist = argv[1:]
for x in mycomdlist:
    sum += eval(x)
print(sum)

#File copy application

