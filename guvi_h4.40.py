def sod(n):
    s=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    return(s)
def pal(n):
    s=0
    m=n
    while n>0:
        r=n%10
        s=(s*10)+r
        n=n//10
    if s==m:
        return(1)
    else:
        return(0)
n=int(input())
k=sod(n)
if pal(k)==1:
    print("YES")
else:
    print("NO")