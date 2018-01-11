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

##
####  TREE
##

class Tree():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def printNode(self):
        buf=[]
        buf.append(str(self.val))
        if self.left== None:
            buf.append("L->")
        else:
            s = 'L->'+str(self.left.val)
            buf.append(s)
        if self.right == None:
            buf.append("R->")
        else:
            s = 'R->'+str(self.right.val)
            buf.append(s)

        str1 = '.'.join(buf)
        print('NODE: %s'%str1)

#
# Print a tree given a root
#

def printTree(root):
    buf = deque()
    output = []
    if not root:
        print '$'
    else:
        buf.append(root)
        count, nextCount = 1, 0
        while count:
            node = buf.popleft()
            if node:
                output.append(node.val)
                count -= 1
                for n in (node.left, node.right):
                    if n:
                        buf.append(n)
                        nextCount += 1
                    else:
                        buf.append(None)
            else:
                output.append('$')
            if not count:
                print output
                output = []
                count, nextCount = nextCount, 0
        # print the remaining all empty leaf node part
        output.extend(['$']*len(buf))
        print output


def main():

    print ('PROGRAM')

def treemain():
    tlist =[]
    for i in range(1,7):
        node = Tree(i)
        tlist.append(node)

    for i in range(len(tlist)):
        if i == 0:
            root=tlist[i]
        node = tlist[i]
        ll = 2*i+1
        rr = 2*i+2
        if (ll < len(tlist)):
            node.left= tlist[ll]
        if (rr < len(tlist)):
            node.right= tlist[rr]

    root.printNode()
    printTree(root)

        

if __name__ == '__main__':
    treemain()

