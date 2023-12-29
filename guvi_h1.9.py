from math import inf
n = int(input())
list = list(map(int,input().split()))
min = inf
x=y=0
for i in range(n):
    for j in range(n):
        if(i != j):
            sum = list[i]+list[j]
            if sum == 0:
                print(list[i],list[j])
                min = sum
                break
            elif (abs(sum - 0)) < (abs(min - 0)):
                min = sum 
                x = i
                y = j
    if min == 0:
        break
if min != 0:
    print(list[x],list[y])