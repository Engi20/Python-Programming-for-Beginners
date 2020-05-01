d={'USA':100,'UK':200,'India':300}

print('UK' in d)
print('USA' not in d)
print(100 in d)

d1={'USA':100,'UK':200,'India':300}
d2={'USA':100,'UK':200,'India':300}
d3={'UK':200,'USA':100, 'India':300}

print(d1 is d2)
print(d1 == d2)

print(d1 is d3)
print(d1 == d3)

d2 = d1
print(d1 is d2)

