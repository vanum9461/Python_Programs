n=int(input())
arr=list(map(int,input().split()))
arr.sort()
b=[]
for i in range(1,len(arr)+1):
    b.append(arr.count(i))
max=b[0]
for i in range(len(b)):
    if(b[i]>max):
        max=b[i]
        t=i+1
   
print(t)
    
