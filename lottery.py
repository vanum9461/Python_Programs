import random
num=random.randint(100,999)
l=list(map(int,str(num)))
lnum=int(input("Enter user number"))
p=list(map(int,str(num)))
c=0
for i in p:
    if(i in l):
        c+=1
if(c==3):
    print("Award is $10,000")
elif(c==2):
    print("Award is $3,000")
else:
    print("Award is $1,000")
    
    
