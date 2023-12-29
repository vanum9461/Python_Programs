n=int(input())
l=list(map(int,input().strip().split()))
c=0
for i in range(len(l)):
    a1=l[i]
    for j in range(i+1,len(l)):
        if(a1<l[j]):
            c+=1
print(c)