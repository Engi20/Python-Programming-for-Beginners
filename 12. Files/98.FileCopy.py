FileRead = open('data.txt','r')
FileWrite = open('copydata.txt','w')

for line in FileRead:
	FileWrite.write( line )

