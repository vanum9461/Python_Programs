"""
class Student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def getmarks(self):
        for i in range(2):
            self.marks.append(input())
    def display(self):
        print(self.name,"got",self.marks)
a=Student("Aman")
a.getmarks()
a.display()
"""
def prime(n):
    k=1
    i=2
    while(i*i<=n):
        if(n%i==0):
            k=0
        i+=1
    return k

def Main():
    n=int(input())
    for i in range(2,n+1):
        if(prime(i)):
            print(i,end=" ")

Main()
    



