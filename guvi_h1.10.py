m,n=map(int,input().split())
l1=list(map(int,input().strip().split()))
l2=list(map(int,input().strip().split()))
c=0
if(n>m):
    print("NO")
else:
    for i in l2:
        if i in l1:
            c+=1
    if(c==n):
        print("YES")
    else:
        print("NO")
    