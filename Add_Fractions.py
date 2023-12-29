"""This is the code for Adding Two Fractions.
The case can be a] denominators are same
                b]denominators different
"""
def gcd(a,b):
    if(a == b): 
        return a 
    if(a > b):
        return gcd(a-b, b) 

    return gcd(a, b-a) 
  
def lcm(a,b): 
    return (a*b) / gcd(a,b) 

def addFraction(num1, den1, num2, den2):
    p=(int)(lcm(den1,den2))
    num1=num1*(int)(p//den1)
    num2=num2*(int)(p//den2)
    ans=num1+num2
    t=gcd(ans,p)
    print("{}/{}".format(ans//t,p//t))

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=list(map(int,input().strip().split(' ')))
        addFraction(arr[0],arr[1],arr[2],arr[3])
