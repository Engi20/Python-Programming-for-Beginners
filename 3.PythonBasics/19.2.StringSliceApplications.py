s='hello'

#First character to Upper case
new_s = s[0].upper() + s[1:]
print(s)
print(new_s)

#Last character to Upper case
new_s = s[0:len(s)-1]+s[-1].upper()
print(new_s)

new_s = s[0:-1]+s[-1].upper()
print(new_s)

#First & Last character to Upper case
new_s = s[0].upper()+s[1:-1]+s[-1].upper()
print(new_s)


