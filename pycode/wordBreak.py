from collections import defaultdict

word = "CatMat"
wset={'Cat', 'Mat', 'Ca', 'tM', 'at', 'C', 'Dog', 'og', 'Do'}

def builddict(wset):

    wdict = dict()
    for s in wset:
        ll = len(s)
        wdict[s]= ll

    return(wdict)

class wordbrks(object):
    def __init__(self):
        self.success = 0
        self.len = 0
        self.words = list()

wordarry = [ wordbrks() for i in range(32)]

def wordBreak(thestring, wdict, frame, thread):

    print (' -->F[%d] (%s) :' %(frame, thestring))
    win = 1
    while (win < 4):
        slice = thestring[:win]
        #
        #if the string is found then proceed further
        #
        if slice in wdict: 
            print('[%d] = %s' % (win, slice))
            wordarry[thread].len += 1
            wordarry[thread].words.append(slice)
            # If the slice is same as the thestring then we are done
            if slice == thestring:
                print (' SUCCESS')
                wordarry[thread].success = 1
                return
            s2 = thestring[win::]
            wordBreak(s2, wdict, frame+1, thread)
        if (frame == 0):
            thread += 1
        win += 1
    # end while
        
    return

def printWords():
    for x in wordarry:
        if x.success != 1:
            continue
        # found something
        print (' ')
        print ('#brks= %d' %(x.len), end="")
        for s in x.words:
            print (' %s ' %(s), end="")
        print (' ')



def main():

    wdict=builddict(wset)

    #print word
    frame = 0
    thread = 0
    wordBreak(word, wdict, frame, thread)
    printWords()


if __name__ == "__main__":
    main()


            
