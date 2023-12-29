"""
import rotate
a=['nama','aman','sanam','manas','alok']
d={i:None for i in a}

def pair():
    l=[]
    for i in d:
        for j in range(1,26):
            if(rotate.rotate_word(i,j) in d):
                l.append(i,j,rotate.rotate_word(i,j))
    l.sort()
    for i in l:
        print(l)
pair()
"""
