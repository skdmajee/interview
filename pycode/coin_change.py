import sys
#
# Recursive approach to finding coin change problem
#

global slist
slist=list()

def min_change(V, C):
    def min_coins(i, aC):
        if aC == 0:
            return 0
        elif i == -1 or aC < 0:
            return float('inf')
        else:
            return min(min_coins(i-1, aC), 1 + min_coins(i, aC-V[i]))
    return min_coins(len(V)-1, C)

def change(coins, m, val):
    global slist
    if val == 0:
        print ('Solution::')
        print slist
        slist = []
        return 1
    elif m == -1 or val < 0:
        return 0
    else:
        #slist.append(coins[m-1])
        #c1 = change(coins, m, val-coins[m-1])
        c1 = 0
        slist.append(coins[m-2])
        c2 = change(coins, m-1, val)
        return(c1+c2)

def main():
    
    coins=[9,5,6,1]
    val = 11
   
    print coins
    print slist
    count = change(coins, len(coins), val)
    print (('Count = %d')%(count))

if __name__ == '__main__':
    main()

