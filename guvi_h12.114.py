def isprime(x):
    if(x>1):
        c=x//2
        f=0
        for i in range(2,c+1):
            if(x%i==0):
                f=1
                break
        if(f==0):
            return 1
        else:
            return 0
    else:
        return 0
        
if __name__ == "__main__":
    l,r=map(int,input().split())
    count=0
    for i in range(l,r+1):
        s=0
        while(i!=0):
            s=s+(i%10)
            i=i//10
        if(isprime(s)):
            count+=1
    print(count)