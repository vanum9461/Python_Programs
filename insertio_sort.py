n=int(input("enter no of elements "))
a=list()
for i in range(n):
    num=int(input())
    a.append(num)
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while(j>=0 and a[j]>key):
        a[j+1]=a[j]
        j-=1

    a[j+1]=key

print("Array",a)
      
