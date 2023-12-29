s=input()
c=0
for i in range(len(s)):
    if(s[i]==" "):
        c+=1 
p=0
l=s.split(" ")
for i in l:
    if i[0].isupper():
        p+=1 
if(p==c+1):
    print("yes")
else:
    print("no")