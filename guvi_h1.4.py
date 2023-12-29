n=int(input())
l=list(map(int,input().strip().split()))
p=0
for i in l:
    p=p^i
print(p)

