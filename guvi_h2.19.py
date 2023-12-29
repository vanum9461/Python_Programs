n,k=map(int,input().split())
p=[]
for i in range(n):
    d=set(map(int,input().split()))
    p.append(d)
c=d.intersection(*p)
print(*c)