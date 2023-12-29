n=int(input())
l=list(map(int,input().strip().split()))
count=0
for i in range(1,len(l)):
    for j in range(i-1,-1,-1):
        if(l[j]<l[i]):
            count+=l[j]
print(count)
