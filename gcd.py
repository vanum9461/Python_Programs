"""
def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if(m%i)==0:
            fm.append(i)
    fn=[]
    for j in range(1,n+1):
        if(n%j)==0:
            fn.append(j)
    cf=[]
    for f in fm:
        if f in fn:
            cf.append(f)
    return (cf[-1])



def gcd(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
            cf.append(i)
    print(*cf)
    return (cf[-1])

p=gcd(16,12)
print(p)         

"""
def gcd(m,n):
    if(n==0 or m%n==0):
        return n
    else:
        return gcd(n,m%n)

#p=gcd(16,12)
#print(p)   
