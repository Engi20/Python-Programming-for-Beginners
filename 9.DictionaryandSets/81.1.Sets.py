s = {'Hello','Hi','Python','Hi','Science'}
print(s)
print(len(s))

l = [10, 'Hello', 2.85, 10, 'Python']
s1 = set(l)
print(s1)
print(len(l))
print(len(s1))

s = {'Hello','Python','Hi','Science'}
print(s)
print(len(s))
s.add('Data')
print(s)
print(len(s))
s.add('Hello')
print(s)
print(len(s))

s.remove('Data')
print(s)
print(len(s))

#print(s[0:2]) #TypeError
#s.remove('USA') #KeyError

#print(s[0]) #TypeError
