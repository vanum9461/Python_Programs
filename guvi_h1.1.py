n=int(input())
arr=list(map(int,input().split()))
arr.sort()
a=[]
for i in range(n-1):
    if (arr[i] not in a) and arr[i]==arr[i+1]:
        a.append(arr[i])
if len(a) == 0:
    print("unique")
else:
    print(*a)