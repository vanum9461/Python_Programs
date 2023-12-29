#print("Hello World")
"""
def gcd(m,n):
    if(n==0 or m%n==0):
        return n
    else:
        return gcd(n,m%n)

def gcd(m,n,o=None):
    if(o==None):
        print("GCD of 2 nos")
    else:
        print("GCD of 3 nos")

print(gcd(2,5))
print(gcd(5,4,3))
"""

def swap(x,y):
    return y,x,z

a=2
b=5
#print(type(swap(a,b)))
a,b,c=swap(a,b,c)
print(a,b,c)
