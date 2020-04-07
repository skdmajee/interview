Strings are the most common data structure and most oft asked interview question. It is important to focus
on the patterns. 

My Biggest weakness is the liit condition:
* careful about what is the terminal condition for a loop or recursion. Recurriosn often looks forzeor value.
* Index value and len. Index starts at zero, however during recusrion anything to do with min/max must account for the last operation. If the index is zero the operation is not counted. I prefer to pass index=len(s) and then comparisons s[i-1] == s[j-1]

Here are some useful resources:  
 1. From [byte-by-byte](https://www.byte-by-byte.com/strings/)
 1. From [hacker-Rank](https://www.hackerrank.com/challenges/two-strings/topics)

Gotchas:
s[start:end] <-- end char is not covered. So in order to cover the last char in string for example  
s[start:end+1]

Basic Patterns:
1. Using a character array instead of Hash:  
Quick and easy. Fixed size
```python    
  char_array=[0 for in range(256)]  
  char_array[ord(c)]
```  
2. Sliding Window: 
  figure out a window size.  
  Slide one place at a time
  
1. Two Pointers:

1. Min-Max Window:

