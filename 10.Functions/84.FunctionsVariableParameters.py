def mysum(*x):
    sum = 0
    for i in x:
        sum = sum + i
    print(sum)

mysum(2, 3)
mysum(2, 3, 5)
mysum(2, 3, 5, 1, 5, 4)
