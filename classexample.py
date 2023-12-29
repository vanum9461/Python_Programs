"""
class abc:
    #constructor
    def __init__(self,val):
        print("Inside class")
        self.val=val
        print("The value is:",val)
a=abc(10)
"""
class abc:
    v=0
    def __init__(self,x):
        abc.v+=1
        self.x=x
        print(abc.v,self.x)
ob1=abc(10)
ob2=abc(30)
