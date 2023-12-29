from math import ceil,floor
t=int(input())
for i in range(t):
    n=int(input())
    left=list(str(n))
    right=list(str(n))
    for j in range(len(left)):
        if(left[j]=='9'):
            left[j]='3'
            right[j]='6'
        elif(left[j]=='8'):
            left[j]='3'
            right[j]='5'
        elif(left[j]=='7'):
            left[j]='2'
            right[j]='5'
        elif(left[j]=='6'):
            left[j]='3'
            right[j]='3'
        elif(left[j]=='5'):
            left[j]='2'
            right[j]='3'
        elif(left[j]=='4'):
            left[j]='2'
            right[j]='2'
        elif(left[j]=='3'):
            left[j]='1'
            right[j]='2'
        elif(left[j]=='2'):
            left[j]='1'
            right[j]='1'
        elif(left[j]=='1'):
            left[j]='0'
            right[j]='1'
    print('Case #'+str(i+1)+":",int("".join(left)),int("".join(right)))
    
            
    
