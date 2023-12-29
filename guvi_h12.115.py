if __name__ == "__main__":
    n=int(input())
    l=[]
    for i in range(2,n+1):
        f=0
        c=i//2
        for j in range(2,c+1):
            if(i%j==0):
                f=1
                break
        if(f==0):
            l.append(i)
count=0
for i in range(len(l)):
    a1=l[i]
    for j in range(i,len(l)):
        if(a1+l[j]==n):
            count+=1
print(count)
    

        

