import collections
from collections import defaultdict

wset={'majee', 'name', 'is', 'my', 'I'}
wset={'majee', 'xyz', 'is', 'my', 'I'}
def builddict(wset):
    '''
    Build a dictionary of words from a set
    '''
    wdict = dict()
    for s in wset:
        ll = len(s)
        wdict[s]= ll

    return(wdict)

def findWord(wdict,s,output):
    '''
    Finds matching words from a string where spaces, tabs etc. are deleted
    This works well as long as all the words appear in dictionary. However if
    a non dict word is present the loop will end prematurely without looking for
    the rest of the word.
    '''

    print('-> [%s]'%(s))
    word=''
    if (len(s)==1):
        if s in wdict:
            output.append(s)
            return True;
        else:
            return False

    for i in range(len(s)):
        word += s[i]
        remaining=s[i+1:]
        if word in wdict:
            output.append(word)
            print('i(%d) %s remain (%s)' %(i,word, remaining))
            ret = findWord(wdict,remaining,output)
            if ret:
                return True

    
    return False

def findWord2(wdict,word,leftover, output):
    '''
    Finds matching words from a string where spaces, tabs etc. are deleted
    This is a classic recursive backtracing loop where every character is added to 
    the existing word and checked for match. Since the main driver scans thru all 
    characters and sets, it checks for all existing word and will skip the words
    that are not found.
    '''
    print('-> [%s]'%(word))
    if (len(word) == 0):
        return True

    if (len(word)==1):
        if word in wdict:
            output.append(word)
            return True;
    
    if word in wdict:
        print('F:[%s]'%(word))
        output.append(word)
        ret = True;

    if (len(leftover) != 0):
        ret= findWord2(wdict, word+leftover[0], leftover[1:], output)
        
    return;

def test():
    
    sentence='mynameismajee'
    wd=builddict(wset)
    output=[]
    #ok = findWord(wd,sentence,output)

    for i in range(len(sentence)):
        c=sentence[i]
        ok = findWord2(wd,c,sentence[i+1:], output)
        
    print ' '.join(output)

if __name__ == "__main__":
    test()



