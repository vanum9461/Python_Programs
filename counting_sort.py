def counting_sort(a):
    m=max(a)
    count=[0]*(m+1)
    for i in a:
        count[i]+=1
    p=0
    for i in range(m+1):
        for j in range(count[i]):
            a[p]=i
            p+=1
    return a

def Main():
    arr=list(map(int,input().strip().split(" ")))
    print(counting_sort(arr))
Main()
