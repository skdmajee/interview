import sys
def change(amount, coins):
	
  '''
  tbl = [0] * (amount+1)
  '''
  tbl = [[0 for j in range(amount+1)] for i in range(len(coins)+1)]
  tbl[1][0] = 1

  for c in coins: 
    for val in range(1, amount+1):
      if c <= val:
        '''
				Subtract the coin and use the residulal value to see if
				there is solution for that. Add the current coin to get 
        total number of coin for this amount
				'''
        res = val -c
        if res == 0:
          tbl[c][val] = 1 
        else:
          tbl[c][val] = tbl[c][res] + 1 
        print "BIGGER: c %d val %d res %d tbl[c][val] %d" % (c,val,res,tbl[c][val])
      else:
        tbl[c][val] = tbl[c-1][val]
        print "SMALLER: c %d val %d tbl[c][val] %d" % (c,val,tbl[c][val])

  last_coin = coins[-1]
  return tbl[last_coin][amount]

def main(argv):
  coins= [1, 2, 3]
  if (len(sys.argv) < 2):
    print "USAGE: coin <amount>"
    return 1
  amt = int(argv[1])
  print "Find amount %s given coins " % (amt)
  min_coins = change(amt, coins)
  print 'the required changes: %d' % (min_coins)

if __name__ == '__main__':
    main(sys.argv)
