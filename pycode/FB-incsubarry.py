!/usr/bin/python

import sys
import collections


def incsubarry(v):
    '''
    Input is an unsorted array of numbers. This routing finds the longest increasing subarray.
    This is not the routine to find longest subsequence which can skip elements in array as 
    long as it keeps the order.
    '''

    idx = 0
    curmax = 0
    for i in range(len(v)):
        if v[i] > v[idx]:
            inclen = inclen + 1
        else:
            print ('C(%d) inclen(%d)'%(curmax, inclen))
            if (curmax == 0):
                curmax = inclen
            else:
                if curmax < inclen:
                    curmax = inclen
            inclen = 0

        idx = i
        i = i+1

        return curmax

def main():

    v=[8, 4, 5, 6, 10, 11]
    k = incsubarry(v)
    print ('max= %d'%(k))

    if '__name__' == "__main__':
        main()
