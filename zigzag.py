"""
Input takes an array and convert it into zig zag array.
Example:
Input:4 1 7 8 2 3
Output:1 3 2 7 4 8

"""

n=int(input("Enter no .of elements"))
l=[]
l=list(map(int,input().split(' ')))
l.sort()
for i in range(1,len(l),2):
    if(i==(len(l)-1)):
        break
    l[i],l[i+1]=l[i+1],l[i]

print(*l)              
                  
