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
                    if (n and n!='$'):
                        buf.append(n)
                        nextCount += 1
                    else:
                        buf.append(None)
            else:
                output.append('$')
            if not count:
                print output
                print ('count(%d) nxtcount(%d)' %(count,nextCount))
                output = []
                count, nextCount = nextCount, 0
        # print the remaining all empty leaf node part
        output.extend(['$']*len(buf))
        print output


def main():

    print ('PROGRAM')

def treePrint_test():
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

def createUnbalancedTree():

    root= Tree(10)
    n1, n2 = Tree(5), Tree(20)
    root.left=n1
    root.right=n2
    n21, n22 = Tree(3), Tree(7)
    n1.left= n21
    n1.right = n22
    n31, n32, n33 = Tree(2), Tree(6), Tree(8)
    n21.left= n31
    n22.left = n32
    n22.right = n33
    return root


def height(root):

    #base case
        if (root == None):
            return 0;

        max_depth = 1 + max(height(root.left), height(root.right))
        return max_depth

def min_height(root):

    #base case
        if (root == None):
            return 0;

        max_depth = 1 + min(height(root.left), height(root.right))
        return max_depth

def bfs_height(root):
    '''
    Does a depth first walk of a tree and calculates min and max height..
    Complexity O(n). 
    '''
    if (root == None):
        return 0, 0

    dq = deque()
    dq.append(root)
    count, nextcount = 1, 0
    max_depth = -1
    min_depth = 100
    depth = 1

    while(count):
        node = dq.popleft()
        if ((node.left == None) and (node.right == None)): 
            if (depth > max_depth):
                max_depth = depth
            if (depth < min_depth):
                min_depth = depth

        for tt in  (node.left, node.right):
            if (tt != None):
                dq.append(tt)
                nextcount += 1

        # Done with L,R child
        count -= 1
        if (count == 0):
            depth += 1
            count = nextcount
            nextcount = 0
    #While

    return max_depth, min_depth

def findLCA(root, k, path):

    if (root == None):
        return None

    if( root.val == k):
        print('(%d) %d :' %(k, root.val))
        path.append(root.val)
        return k 

    r1= findLCA(root.left, k, path)
    if (r1 == None):
        r1 = findLCA(root.right, k, path)

    if (r1 == k):
        path.append(root.val)
        print('(%d) %d :' %(k, root.val))
        return k
    
    return None
   



    


#
#  ################################  #



def treetest():

    print('Height of a tree')
    root = createUnbalancedTree()
    depth = height(root)
    mind = min_height(root)
    print('Tree height= %d min= %d)'% (depth, mind))

    depth,dmin = bfs_height(root)    
    print('Tree height= %d min= %d)'% (depth, dmin))

def LCATree():
    print('Given two nodes find common ancestor')
    root = createUnbalancedTree()
    printTree(root)
    path8=[]
    path2=[]
    
    node = findLCA(root, 8, path8)
    node = findLCA(root, 2, path2)

    lcaroot = None
    l = min(len(path2),len(path8))
    if (len(path2)!= 0 and len(path8)!=0):
         while (l):
            v1, v2=path2.pop(),path8.pop()
            if (v1 != v2):
                break
            else:
                lcaroot = v1
            l=l-1
    else:
        lcaroot = root.val

    print('lcaroot= %d' %(lcaroot))
    

    

if __name__ == '__main__':
    #treetest()
    LCATree()

