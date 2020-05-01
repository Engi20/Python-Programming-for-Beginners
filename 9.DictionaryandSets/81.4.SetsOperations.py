s1 = {'USA','UK','India','Australia'}
s2 = {'Australia','USA','Canada'}

print(s1)
print(s2)

s3 = s1 & s2
print(s3)

s3 = s1.intersection(s2)
print(s3)

s3 = s1 | s2
print(s3)

s3 = s1.union(s2)
print(s3)

s3 = s1 - s2
print(s3)

s3 = s2 - s1
print(s3)
