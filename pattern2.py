print("Enter value of n:")
n=int(input())
p=n+1
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j>=p-i):
            print('*',end='')
        else:
            print(' ',end='')
    print('\r')