def findmajority(a):
    mi=0
    c=1
    for i in range(len(a)):
        if(a[mi]==a[i]):
            c+=1
        else:
            c-=1
        if(c==0):
            mi=i
            c=1
    return a[mi]

def checkmajority(a,x):
    c=0
    for i in range(len(a)):
        if(a[i]==x):
            c+=1
    if(c>(len(a)//2)):
        print("Majority element exist")
    else:
        print("not exist")


n=int(input("Enter no of elements "))
a=[]
for i in range(n):
    a.append(input())
print(*a)
p=findmajority(a)
checkmajority(a,p)
