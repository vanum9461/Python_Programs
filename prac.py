"""class akash:
    def __init__(self,length,breadth,height):
        self.length=length
        self.height=height
        self.breadth=breadth
    def peri(self):
        perimeter=self.length+self.breadth+self.height
        return(perimeter)

class aman(akash):
    def __init__(self,length,breadth,height):
        super().__init__(length,breadth,height)
    def area(self):
        ar=self.length+self.breadth+self.height
        return(ar)


am=aman(10,20,30)
print(am.area())
"""

def akash(n):
    if(n<=0):
        return 0
        
    else:
        c= n%10+akash(n//10)
        su=c%10+c//10
        """su=0
        while(c>0):
            rev=c%10
            su+=rev
            c=c//10"""
        return(su)
            
n=int(input("Enter the number: "))
print(akash(n))
