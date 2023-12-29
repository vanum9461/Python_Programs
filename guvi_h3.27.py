x=str(input())
f=1
l=len(x)
while(l>0):
    re=x[::-1]
    if(x==re):
        l = len(x)
        x = x[:l - 1]
    else:
        f = 0
        print(x)
        break