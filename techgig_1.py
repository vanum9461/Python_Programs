#WIN OR LOSE
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    b=list(map(int,input().strip().split()))
    a.sort()
    b.sort()
    c=0
    for j in range(n):
        if(b[j]>=a[j]):
            c+=1 
    if(c==n):
        print("WIN",sep='\n')
    else:
        print("LOSE",sep='\n')
