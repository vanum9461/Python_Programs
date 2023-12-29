n,k=map(int,input().strip().split())
l=list(map(int,input().strip().split()))
c=0
for i in range(n):
    for j in range(n):
        if(l[i]+l[j]==k):
            c=1
            break
if(c==1):
    print('YES')
else:
    print('NO')