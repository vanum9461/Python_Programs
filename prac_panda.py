import pandas as pd

"""
l=[7,9,12]
r=pd.Series(l*2,index=range(10,16))
s=r*3
print(r)
print(s)


L=['Harish','Nikhil','Richard','Naveen','Vijay']
sr=pd.Series(L,index=['a','b','c','d','e'])

print(sr[1:3])
print(sr[2:])
print(sr[['b','d','e']])

sr[2]='ravi'
print(sr)


t=pd.Series(data=range(10,20,2),index=range(1001,1006))
print(t.head(4))
print()
print(t.tail())
"""

basic_pay=pd.Series([20000,10000,30000,5000,60000])
da=0.4*basic_pay
pf=0.3*basic_pay
extra=da-pf
net_salary=basic_pay+extra
print(net_salary)
