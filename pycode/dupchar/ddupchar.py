#!/usr/bin/python
import sys 

def ddup(mstr):

    '''
    Given a string this will take out all duplicate characters and order i.e. alter the 
    original string an create a new alphabetically ordered string.
    '''

    chlst = [ [] for i in range(ord('z') - ord('a')+1)]

    for i in range(len(chlst)):
        ll = chlst[i]
        ll.append(0)
        ll.append(chr(i+ord('a')))
    print chlst

    for ch in mstr:
        idx = ord(ch) - ord('a')
        print "ch= "+ch
        chlst[idx][0] += 1

    '''
    Now collect the characters back in a list
    '''
    ss = ""
    for i in range(len(chlst)):
        if chlst[i][0] > 0:
            ss += chlst[i][1]

    return ss

def dduplex(mstr):
    '''
    Given a string, it will remove all duplicate characters and will produce set that has lowest 
    lexical order. What it means that the original order of char MUST not be altered while producing
    this new string.
    So if the input xcacdb then the result is xacdb. Even thoug x has higer ordinal
    value it still happens to be the first character and there is no duplicate.
    '''

    '''
    For each ch in the string we note the ch and the position in the string.
    when there is a duplicate, then 
        if there is lower ordinal found in the preceeding string then this is 
        new position for this particular character.
    '''
    tbl = [ [] for i in range(len(mstr)+1)]
    d = dict()
    i = 0
    maxord = ord('a')

    for ch in mstr:
        ll = tbl[i]
        if ch in d.keys():
            # This char exists
            chx = d[ch]
            chx[0] += 1
            # Compare the ordinal number with the max ordinal upto this point
            if ord(ch) >= maxord:
                chx[2] = i
        else:
            chx=list()
            #Remeber frequency and the character
            chx.append(1)
            chx.append(ch)
            # Remeber the position
            chx.append(i)
            d[ch] = chx
            if ord(ch) > maxord:
                maxord = ord(ch)
            print "maxord = "+chr(maxord)

        # incr the index
        i += 1

    return d

import json
import collections
def my_print(x):
    return json.dumps(x)

def main(argv):

    mstr="bcabc"
    if (len(sys.argv) < 2):
        print "USAGE: ddupchar <string>"
        return 1

    mstr=argv[1]
    #xx = ddup(mstr)
    #print "final string : "+xx
    dd = dduplex(mstr)
    print my_print(dd) 

if __name__ == '__main__':
    main(sys.argv)


