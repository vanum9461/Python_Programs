# cook your dish here
t=int(input())
while(t>0):
    c=0
    d=0
    n,k=map(int,input().strip().split())
    arr=list(map(int,input().strip().split()))
    arr.sort(reverse=True)
    print(*arr)
    for i in range(k):
        if(arr[i]==arr[k]):
            c+=1
        d+=1
    print(c+d)
    t-=1
            
