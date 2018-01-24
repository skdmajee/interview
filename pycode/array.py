
#!/usr/bin/python

import sys
import collections
from collections import deque
from collections import namedtuple 
from collections import Counter

#
# Some basic pycode classes 
#

##
#####   STACK  
##
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)



#
###  Array related problems. 
#

def substringProduct(a, K, output):
    '''
    Relates to finding matching substring whose products are <K or more than K
    '''

    div=1
    prod=[0]*len(a)

    prod[0]= mult=a[0]
    for i in xrange(1,len(a)):
        if ((a[i] == 0) or (mult == 0)):
            break
        prod[i]=mult*a[i]
        mult=prod[i]
        if mult < K:
            s=a[:i+1]
            print s
            output.append(s)

    print prod
    # Done

    for i in xrange(1,len(prod)):
        div=prod[i-1]
        j=i
        print ('div[%d]'%prod[i-1])
        while j<len(prod):
            if (prod[j] != 0 and div != 0):
                prod[j] = prod[j]/div
            if prod[j] < K and j>i:
                s=a[i:j+1]
                print  s
                output.append(s)
            j += 1
        #while
        print 'PROD', prod
    #for

    return output







def main():
    print ('PROGRAM')

    output=[]
    a=[2,3,6,1,5]
    output = substringProduct(a, 13, output)
    print output


        

if __name__ == '__main__':
    main()

