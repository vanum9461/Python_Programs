import urllib.request
import os.path
filename="hello.txt"
#print(data.read())
d=[0]*26
def countLetters(line,ls):
    for ch in line:
        if ch.isalpha():
            ls[ord(ch)-ord('a')]+=1

if os.path.isfile(filename):
    #f=open(filename,"r")
    data=urllib.request.urlopen("https://gitlab.com")
    content=data.read().decode()
    countLetters(content.lower(),d)
    for i in range(26):
        print(chr(ord('a')+i),":",str(d[i]))


