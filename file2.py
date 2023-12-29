#count the no.of characters from a file and its frequency.

import os.path
filename="hello1.txt"
d=[0]*26
def countLetters(line,ls):
    for ch in line:
        if ch.isalpha():
            ls[ord(ch)-ord('a')]+=1
            
if os.path.isfile(filename):
    f=open(filename,"r")
    for line in f:
        countLetters(line.lower(),d)
    for i in range(26):
        print(chr(ord('a')+i),":",str(d[i]))
