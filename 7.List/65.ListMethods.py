l = [10, 'Hello', 2.85]

print(l)
l.insert(1,20)
print(l)
print(len(l))

l.insert(8,30)
print(l)
print(len(l))

l.append(78.5)
print(l)
print(len(l))

#l.append(40,50) #Takes only One argument

l.extend([40,50])
print(l)
print(len(l))

l[1] = 45
print(l)

del(l[3])
print(l)
print(len(l))
