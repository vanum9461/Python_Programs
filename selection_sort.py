n=int(input("enter no of elements "))
a=list()
for i in range(n):
  num=int(input())
  a.append(num)
for i in range(len(a)):
    min=i
    for j in range(i+1,len(a)):
        if a[j]<a[min]:
            min=j 
            
    a[i],a[min]=a[min],a[i]        
    
print("Array",a)
            
