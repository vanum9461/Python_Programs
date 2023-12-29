print("Enter value of n:")
n=int(input())
for i in range(n):
    for j in range(n):
        if(j<=i):
            print('*',end='')
    print('\r')

'''
n=5

*
**
***
****
*****

'''