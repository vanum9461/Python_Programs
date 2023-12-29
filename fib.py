from time import time

def fib(n):
    if(n<=1):
        return n
p    F=[]
    F.append(0)
    F.append(1)
    for i in range(2,n+1):
        F.append(F[i-2]+F[i-1])
    return F[n];

def Main():
    n=int(input())
    print(fib(n))


start=time()
Main()
end=time()
print(end-start)
