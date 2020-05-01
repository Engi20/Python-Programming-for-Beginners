
try:
    FileRead = open('data.txt','r')
    contents = FileRead.read()
    print(contents)
except IOError as e:
    print(e)


