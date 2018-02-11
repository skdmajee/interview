import sys

def lonely_integer(a):
    xor=a[0]
    for i in xrange(1,len(a)):
        xor= (xor)^(a[i])
    return xor
    

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)
