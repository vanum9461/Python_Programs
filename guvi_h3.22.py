n=int(input())
l=list(map(int,input().strip().split()))
q=[]
for i in range(n):
    p=1
    for j in range(n):
        if(i!=j):
            p*=l[j]
    q.append(p)
print(*q)
    
    
    