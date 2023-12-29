t=int(input())
for i in range(t):
    D=int(input())
    l=[]
    for j in range(D):
        l=list(map(int,input().strip().split()))
    Q=int(input())
    for k in range(Q):
        de,re=map(int,input().strip().split())
        c=0
        for k in range(D):
            if(de>=l[k][0]):
                c+=l[k][1]
        if(c>=re):
            print("Go Camp")
        else:
            print("Go Sleep")
    

        
