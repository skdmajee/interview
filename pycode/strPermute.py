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

def permute(sostr, s):
    if len(s) == 1:
        print "STR= %s" % (sostr+s)
        return
    else:
        pos = 0
        for ch in s:
            leftout = s[:pos] + s[pos+1::]
            permute(sostr + ch, leftout)
            pos += 1
    return

def recSubset(sofar, rest, side):
   
    print "recSub-->>[%s]: sofar(%s) rest(%s)" %(side, sofar, rest)
    if len(rest) == 0:
        print "SET:: %s" %(sofar)
    else:
        ' include the char from string'
        recSubset(sofar + rest[0], rest[1::], "TOP")
        recSubset(sofar, rest[1::], "BOT")
        ' exclude the char from string'


def removeDuplicate(s):
    a = ''.join(sorted(s))
    lastch = None
    ss=''
    for ch in a:
        if lastch != ch:
            ss += ch
        lastch = ch

    print "fixed string = %s"+ss
    return ss 

def main2():

    ss = "ABCADC"
    ss="ABC"
    s = removeDuplicate(ss)

    pos = 0
    for ch in s:
        ss = ch
        leftout = s[:pos] + s[pos+1::]
        print "..main: ch(%s) leftout(%s)" % (ch, leftout)
        permute(ss, leftout)
        pos += 1

    print "original : "+s
    rest = s;
    pattern = ''
    recSubset(pattern, rest, "TOP")
    

if __name__ == '__main__':
    main2()
