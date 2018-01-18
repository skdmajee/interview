#!/usr/bin/python

import sys
import json
import collections

def recPermute(sofar, leftout):
    print ".....ENTRY(recPermute): sofar(%s) leftout(%s)" % (sofar, leftout)
    pos = 0
    if len(leftout) == 1:
        print "STR= %s" % (sofar+leftout)
        return
    for ch in leftout:
        remaining = leftout[:pos]+leftout[pos+1::]
        recPermute(sofar + ch, remaining)
        pos += 1
        print "......POST::  pos(%d) left(%s) sofar(%s)->" %(pos, leftout,sofar)


def main1():
    leftout="ABCD"
    sofar=""

    recPermute(sofar, leftout)

def permute(sostr, rest, output):
    '''
    This is a permutation, so for n items, n characters N! is available
    '''
    if len(rest) == 0:
        #print "STR= %s" % (sostr+s)
        output.append(sostr)
        return
    else:
        for i in range(len(rest)):
            leftout = rest[:i] + rest[i+1::]
            permute(sostr + rest[i], leftout,output)
    return

def recSubset(sofar, rest, side, output):
   
    #print "recSub-->>[%s]: sofar(%s) rest(%s)" %(side, sofar, rest)
    if len(rest) == 0:
        #print "SET:: %s" %(sofar)
        output.append(sofar)
    else:
        ' include the char from string'
        recSubset(sofar + rest[0], rest[1::], "TOP", output)
        recSubset(sofar, rest[1::], "BOT", output)
        ' exclude the char from string'


def removeDuplicate(s):
    a = ''.join(sorted(s))
    lastch = None
    ss=''
    for ch in a:
        if lastch != ch:
            ss += ch
        lastch = ch
    return ss 

#####
##

def main2():

    ss = "ABCADC"
    s = removeDuplicate(ss)
    print('REMOVE DUPLICATE:: orig[%s] Clean[%s]'%(ss,s))
    print('################################')
    print
    print

    s="ABC"
    print('PERMUTE STRING: [%s]'%(s))
    output=[]
    for i in range(len(s)):
        sofar = s[i]
        leftout = s[:i] + s[i+1:]
        #print "..main: sofar(%s) leftout(%s)" % (sofar, leftout)
        permute(sofar, leftout,output)

    print ' '.join(output)
    print('################################')
    print
    print

    print('all subset of a string[%s]'%s)
    rest = s;
    pattern = ''
    output=[]
    recSubset(pattern, rest, "TOP", output)
    print ' '.join(output)
    print('################################')
    print
    print
    

if __name__ == '__main__':
    main2()
