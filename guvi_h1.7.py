n = int(input())
array = list(map(int,input().split()))
for i in range(n):
    if array[i]%2==0 and i%2 !=0:
        print(array[i], end=' ')
    elif array[i]%2 !=0 and i%2 ==0:
        print(array[i], end=' ')