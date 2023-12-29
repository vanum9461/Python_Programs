
"""
def isprime(n):
    l=[]
    if(n>1):
        for i in range(1,n+1):
            if(n%i==0):
                l.append(i)
        #print(l)
        if(l==[1,n]):
            return 1
        else:
            return 0
    else:
        return 0
"""
def isprime(n):
    l=[1]*(n+1)
    p=2
    while((p*p)<=n):
        if(l[p]==1):
            for i in range(p*2,n+1,p):
                l[i]=0
        p+=1
    for j in range(2,n):
        if(l[j]):
            print(j)
def check():
    isprime(100)
check()         
        
        

        
"""    
def values():
    p=[]
    for i in range(1000):
        c=isprime(i)
        if(c==1):
            p.append(i)
    print(p)
    
values()
"""
