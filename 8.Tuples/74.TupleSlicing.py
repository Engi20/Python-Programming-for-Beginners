t = (10, 'Hello', 2.85, 56.5, 'Python')

print(t)

print(t[0:3])
print(t[3:5])
print(t[3:7]) # No Error

print(t[::2])
print(t[0:8:2])

print(t[::-2])

print(t[:-5])
print(t[-3:])


t1 = t[:]
print(t)
print(t1)

