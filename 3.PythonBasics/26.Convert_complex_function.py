print(complex(10)) #real value
print(complex(2,3)) #real and imaginary value
print(complex(2,-4)) #real and imaginary value

print(complex(10.75)) #real value
print(complex(2.25,3)) #real and imaginary value
print(complex(2,3.75)) #real and imaginary value
print(complex(2.25,4.75)) #real and imaginary value

print(complex(0b1001)) #real value
print(complex(0b1001,3)) #real and imaginary value
print(complex(0b1001,0b1101)) #real and imaginary value

print(complex(0o37)) #real value
print(complex(0o37,3)) #real and imaginary value
print(complex(0o37,0o71)) #real and imaginary value

print(complex(0x2F)) #real value
print(complex(0x2F,3)) #real and imaginary value
print(complex(0x2F,0xA4)) #real and imaginary value

print(complex(0x2F,0b1101)) #real and imaginary value
print(complex(0x2F,0o71)) #real and imaginary value
print(complex(0b1101,0o71)) #real and imaginary value

print(complex('2'))
#print(complex('2',3)) Not Possible
#print(complex(2,'3')) Not Possible
#print(complex('2','3')) #Not Possible
print(complex('2+3j'))
print(complex('2.25+3.75j'))
#print(complex('0b1001+3.75j')) Not Possible
#print(complex('0x2F+3.75j')) Not Possible
#print(complex('0o27+3.75j'))

print(complex(True))
print(complex(True,True))
print(complex(True,False))
print(complex(False,True))

#print(complex(None)) Not Possible

