n=int(input("enter no"))
a=list()
s=0
for i in range(n):
    num=int(input())
    a.append(num)

for i in range(n):
    c=0
    for j in range(2,a[i]):
        if(a[i]%j==0):
            c=1
            break
    if(c==0):
        s+=a[i]

print(s)
