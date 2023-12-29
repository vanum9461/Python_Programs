n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=max(l)
k=l.index(l2)
l1.append(l2)
for i in range(k+1,len(l)):
    max=i
    for j in range(i,len(l)): 
        if l[j]>max:
            max=l[j]
    if max==i:
        l1.append(l[i])
print(*l1)
print(l2)