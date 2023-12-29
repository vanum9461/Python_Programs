n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n+1):
    if n*i in a:
        c=c+1
print(c)