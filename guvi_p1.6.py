n=int(input())
l=list(map(int,input().strip().split()))
count=0
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        if(l[i]<l[j]):
            for k in range(j+1,len(l)):
                if(l[j]<l[k]):
                    count+=1
print(count)
