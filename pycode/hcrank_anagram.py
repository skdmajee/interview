#!/usr/bin/python

import sys
import collections
from collections import deque
from collections import namedtuple 
from collections import Counter

def numbers_needed(a,b):
    wd = dict()

    remove=0
    for i in xrange(len(a)):
        c=a[i]
        if c in wd:
            wd[c]=wd[c]+1
        else:
            wd[c]=1
        remove +=1
    # done processing 

    for i in xrange(len(b)):
        c=b[i]
        if c in wd:
            f=wd[c]
            if f <=0:
                remove +=1
            else:
                wd[c]=f-1
                remove-=1
        else:
            remove+=1
    return remove
                
def main():

    print ('PROGRAM')
    a = raw_input().strip()
    b=raw_input().strip()

    print numbers_needed(a,b)

if __name__ == '__main__':
    main()

