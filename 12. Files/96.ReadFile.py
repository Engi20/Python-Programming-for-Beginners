FileRead = open('data.txt','r')
contents = FileRead.read()
print(contents)

line_content = FileRead.readlines()
print(line_content)
l = line_content
for i in l:
    print(i)

for line in FileRead:
	print(line)

