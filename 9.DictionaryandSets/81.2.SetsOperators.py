s = {'Hello','Hi','Python','Hi','Science'}

print('Hi' in s)

s1={'Hello','Hi','Python','Hi','Science'}
s2={'Hello','Hi','Python','Hi','Science'}
s3={'Python','Hi','Science','Hello','Hi'}

print(s1 is s2)
print(s1 == s2)

print(s1 is s3)
print(s1 == s3)

s2 = s1
print(s1 is s2)
