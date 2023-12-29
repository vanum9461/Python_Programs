file=open("hello.txt","r")
l=file.read()
li=l.split()
p=[]
for i in li:
    p.append(li.count(i))
#print(*(zip(li,p)))
c=zip(li,p)
m=dict(c)
print(m)
#ignore case
