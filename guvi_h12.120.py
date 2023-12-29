n=int(input())
l=list(map(int,input().strip().split()))
c=0
for i in range(len(l)):
    a1=l[i]
    for j in range(i+1,len(l)):
        a2=l[j]
        for k in range(j+1,len(l)):
            if(a1+a2==l[k]):
                c+=1
print(c)