n=int(input("enter no of elements"))
a=[]
for j in range(n):
    a.append(int(input()))
max=len(a[0])
temp=a[0]
for i in a:
    if(len(a[i])>max):
        max=len(a[i])
        temp=a[i]
print(temp,"is the max number with length of",max)
