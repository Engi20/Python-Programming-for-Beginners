def myadd(b):
    global a
    a = b + 2
    print(a)
    return a

a = 10
c = myadd(a)
print(a)
print(c)

