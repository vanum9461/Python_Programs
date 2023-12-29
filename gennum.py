import random
l=[]
l2=[False]*99
for i in range(100):
    x=random.randint(1,99)
    l.append(x)
for i in l:
    l2[i]=True
print(*l)
print(*l2)
if l==True:
    print("Yes")
else:
    print("No")



    
    


