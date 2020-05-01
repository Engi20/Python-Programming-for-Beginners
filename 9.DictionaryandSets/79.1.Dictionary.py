d={'USA':100,'UK':200,'India':300}
print(d)
print(len(d))

d={'USA':'America', 'UK':[200,'London'],'India':(300,10)}
print(d)
print(len(d))

#print(d[0]) #Cannot use indexing

print(d['USA'])
#print(d['Usa']) #KeyError
print(d['UK'])
print(d['India'])

print(d['USA'])
print(type(d['USA']))
print(d['UK'])
print(type(d['UK']))
print(d['India'])
print(type(d['India']))

d={'USA':100,'UK':200,'India':300}
print(d)
print(len(d))
d['Aus'] = 400
print(d)
print(len(d))

del(d['UK'])
print(d)
print(len(d))

#del(d['usa']) #KeyError

print(d.keys())
print(d.values())

