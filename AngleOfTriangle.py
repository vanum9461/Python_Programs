"""import math

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
y3=int(input())

a=sqrt(pow((x3-x2),2)+pow((y3-y2),2))
b=sqrt(pow((x3-x1),2)+pow((y3-y1),2))
c=sqrt(pow((x2-x1),2)+pow((y2-y1),2))

A=acos((a*a-b*b
"""

from math import *
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
a=((x2-x1)**2+(y2-y1)**2)**0.5
b=((x1-x3)**2+(y1-y3)**2)**0.5
c=((x3-x2)**2+(y3-y2)**2)**0.5
A=degrees(acos((a**2-b**2-c**2)/(-2*b*c)))
B=degrees(acos((-a**2+b**2-c**2)/(-2*a*c)))
C=degrees(acos((-a**2-b**2+c**2)/(-2*b*a)))
print(round(A,2),round(B,2),round(C,2))
