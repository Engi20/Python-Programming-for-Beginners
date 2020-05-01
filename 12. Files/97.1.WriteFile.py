FileWrite = open('datawrite.txt','w')

FileWrite.write('File writing line-1\n')
FileWrite.write('File writing line-2\n')
FileWrite.write('File writing line-3\n')

L = [ 10, 20, 30, 40 ]
for line in L:
	FileWrite.write(str(line) + '\n')

