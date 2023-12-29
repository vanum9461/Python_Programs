n = int(input())
arr = list(map(int,input().split()))
res = []
flag = True
for i in range(n):
    if arr[i] not in res:
        res.append(arr[i])
    else:
        print(arr[i])
        flag = False
        break
if flag == True:
    print('unique')