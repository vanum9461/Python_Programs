n=int(input())
l=list(map(int,input().strip().split()))
p=[]
for i in range(len(l)):
    if(i==l[i]):
        p.append(i)
if(p==[]):
        print(-1)
else:
        print(*p)

