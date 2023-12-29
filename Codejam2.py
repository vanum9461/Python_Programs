t=int(input())
for j in range(t):
    n=int(input())
    string=input()
    string2=""
    for i in string:
        if(i=='E'):
            string2+='S'
        else:
            string2+='E'
    print('Case #'+str(j+1)+":",string2)
