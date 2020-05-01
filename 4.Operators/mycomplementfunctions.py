def flip(c):
    return '1' if (c == '0') else '0'

def ones(bin):
    n = len(bin)
    ones = ''
    for i in range(n):
        ones += flip(bin[i])

    if n==31:
        print(1,*ones, sep='')
        return '1'+ones
    if n==32:
        print(*ones,sep='')
        return ones

def twos(bin):
    n = len(bin)
    ones = ''
    twos = ''
    for i in range(n):
        ones += flip(bin[i])
    ones = list(ones.strip(''))
    twos = list(ones)
    for i in range(n - 1, -1, -1):
        if (ones[i] == '1'):
            twos[i] = '0'
        else:
            twos[i] = '1'
            break
    if (i == -1):
        twos.insert(0, '1')

    if n==31:
        print(1,*twos, sep='')
    if n==32:
        print(*twos,sep='')

def mybin(n):
#    if n < 0:
#        print('1'+'{:032b}'.format(n))
#        return '1'+'{:032b}'.format(n)
#    else:
#        print('{:032b}'.format(n))
#        return '{:032b}'.format(n)
    print('{:032b}'.format(n))
    return '{:032b}'.format(n)

def convert(n):
    print(int(n))
