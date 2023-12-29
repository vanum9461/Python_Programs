def bubble_sort(a):
    c=0
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                c+=1
    print(c)
    return a
def Main():
    arr=list(map(int,input().strip().split(" ")))
    print(bubble_sort(arr))
Main()
