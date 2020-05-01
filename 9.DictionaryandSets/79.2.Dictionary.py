d={'USA':100,'UK':200,'India':300}

#d1 = d + {'Aus':400} Cannot Use

#d.insert('Aus',400) #AttributeError

#d.append('Aus',400) #AttributeError

#d.extend({'Aus':400}) #AttributeError

#print(d[0:2]) #TypeError

print(d)
del(d['UK'])
print(d)

#d.sort() #AttributeError


