#!/usr/bin/python

import sys
import collections

#
# Find the longest increasing subsequence out of a given vector
# Algo:
#  L[0] = v[0]
#  Assume L[i] represents the LIS for subarray upto i,
#  For each v in v[]:
#    for all L 0...i:
#        find the longest L so far
#        If v[i] > tail of that list then 
#           copy and extend the longest list
#        else
#           find the longest list where tail < v[i]
#

class LIS():
    def __init__(self, tail, len):
        self.tail = tail
        self. len = len

    def pp(self):
        print('LISOBJ: %d:%d '%(self.len, self.tail))

def longestIncSeq(v):
  
#L=[ [] for i in range(len(v))]
    L=[]
    for i in range(len(v)):
        L.append(LIS(0,-1))
    maxll = 0
    L[0] = LIS(v[0], 1)
 
    for i in range(1, len(v)):
        print('v[%d] %d maxll(%d)' %(i,v[i],  maxll))
        lismax = L[maxll]
        if (lismax.tail < v[i]):
            L[i] = LIS(v[i], lismax.len+1)
            maxll = i
            print ('Extend: L[%d] (L:T) %d:%d max=%d' %(i, L[i].len, L[i].tail, maxll))
            continue
        else:
            mlen = -1
            llong = -1
            for j in range(len(L)):
                if (j < i):
                    lis = L[j]
                    lis.pp()
                    if lis.tail < v[i]:
                        if mlen < lis.len:
                            llong = j
                            mlen = lis.len
            #
            # may be found one
            #
            if (llong != -1):
                print ('next longest %d' % (llong))
                L[i].len = L[llong].len + 1
                L[i].tail = v[i]

    # End For loop
    return L

def main():
    v= [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13]

    LL = longestIncSeq(v)
    for i in range (len(LL)): 
        print ('LL[%d]= len(%d):tail(%d)' %(i, LL[i].len, LL[i].tail))

if __name__ == "__main__":
    main()

                    
                
            
            
            

      
    
