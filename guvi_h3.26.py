n=int(input())
a=list(map(int,input().split()))
for i in range(n-1,0,-1):
    print(a[i],end='->')
print(a[0])