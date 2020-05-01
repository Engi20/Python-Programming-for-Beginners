FileWrite = open('datawrite.txt','a')

L = [55,65,75]
for line in L:
	FileWrite.write(str(line) + '\n')

