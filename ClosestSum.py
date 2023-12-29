n=int(input())
l=list(map(int,input().strip().split()))
for i in range(len(l)):
    for j in range(len(l)):
        if(i!=j):
            q=l[i]+l[j]
            if(q==0):
                print(l[i],l[j])
                break

            