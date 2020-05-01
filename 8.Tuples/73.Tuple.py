t = (1, 3, 2, 1, 2, 5, 3, 2)
print(t)
print(type(t))
print(len(t))

t = (10, 'Hello', 2.85)
print(t)
print(len(t))

print(t[0])
print(type(t[0]))
print(type(t[1]))
print(type(t[2]))

#print(t[5]) #IndexError

print(t[-1])
print(t[-2])
#print(t[-6]) #IndexError

t1 = t + (56.5, 'Python')
print(t1)
print(len(t1))

#t[0] = 20 #Typeerror
#t.insert(1,20) #Attribute Error
#t.append(78.5) #Attribute Error
#t.extend((40,50)) #Attribute Error
#del(t[0]) #Type Error



