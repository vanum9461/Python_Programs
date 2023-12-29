import math
n=int(input("enter no. of entries"))
a=[]
for i in range(0,n):
    a.append(int(input()))
print(*a)
av=sum(a)//n
print("Average is ",av)
if(av>=80 and av<=100):
    print("Grade A")
elif(av>=60 and av<80):
    print("Grade B")
else:
    print("Grade C")
    
