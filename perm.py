 
from itertools import permutations 
word=input("Enter:")
l=[]
#print([word[i:i+1] for i in range(0, len(word), 1)])
for i in word:
    l.append(i)
print(l)
perm = permutations(l) 
for i in list(perm): 
	print(i) 

