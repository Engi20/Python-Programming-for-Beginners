l = [10,20,30,40]

#print(l[10])
#print(l)

try:
    print(l[10])
except IndexError as e:
    print(e)

print(l)

