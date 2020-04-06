Strings are the most common data structure and most oft asked interview question. It is important to focus
on the patterns. 

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

