n=int(input())
l=list(map(int,input().strip().split()))
l.sort()
i,j=0,n-1
while(i<j):
    print(l[j],end=" ") 
    j-= 1
    print(l[i],end=" ") 
    i+= 1
if (n%2!=0): 
    print(l[i])