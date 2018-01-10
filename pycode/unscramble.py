from collections import defaultdict

word = "CatMat"
wset={'Cat', 'Mat', 'Ca', 'tM', 'at', 'C', 'Dog', 'og', 'Do'}

def builddict(wset):

    wdict = dict()
    for s in wset:
        ll = len(s)
        wdict[s]= ll

    return(wdict)

def wordBreak(thestring, wdict):

    win = 1
    while (win < 4):
        slice = thestring[:win]
        #
        #if the string is found then proceed further
        #
        if slice in wdict: 
            print('[%d] = %s' % (win, slice))
            # If the slice is same as the thestring then we are done
            if slice == thestring:
                printf ' SUCCESS'
                return
            else:
                s2 = thestring[win::]
                wordBreak(s2, thedict)

        win += 1
        return

def main():

    wdict=builddict(wset)
    print wdict

    print word
    wordBreak(word, wdict)


if __name__ == "__main__":
    main()


            
