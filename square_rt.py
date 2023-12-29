
"""
# program for square root
"""num=float(input("Enter a number"))
ans=num**0.5
print(ans)
"""


#program for area of triangle
"""
a=float(input("enter first no"))
b=float(input("enter second no"))
c=float(input("enter third no"))

s=(a+b+c)/2

ans=s*(s-a)*(s-b)*(s-c)
rslt=ans**0.5
print("The area of triangle is %0.2f" %rslt)
"""

#print ("i m aman" *5)

#positive,negative,zero
"""
n=float(input("enter a number "))
if n>0:
    print("positive number")
elif n==0:
    print("Zero")
else:
    print("Negative no")
"""

#factorial
"""
n=int(input("enter a number "))
f=1
for i in range(1,n+1):
    f=f*i
print("Factorial of",n,"is",f)
"""

#factorial using recursion

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

m=int(input("enter a number "))
print("factorial of",m,"is",fac(m))
"""
#check no is prime or not

n=int(input("enter any no "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
        else:
            print(n," is prime")
else:
    print(n,"is not prime")
                  







