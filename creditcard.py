def getsize(n):
    c=0
    while(n!=0):
        c+=1
        n=n//10
    return c

def sumofevenplace(n):
    n=n//10
    sum=0
    while(n!=0):
        r=n%10
        sum+=(doublecheck(r*2))
        n=n//100

    return sum

def sumofoddplace(n):
    s=0
    while(n!=0):
        r=n%10
        s+=r
        n=n//100

    return s

def doublecheck(n):
    if(n<9):
        return n
    else:
        return (n//10+n%10)

def prefixmatched(n,k):
    m=getsize(k)
    c=n-k
    while(c!=0):
        n=n//10
        c-=1
    if(n==k):
        return 1
    else:
        return 0

def isvalid(number):
    return((getsize(number) >= 13 and
               getsize(number) <= 16) and
               (prefixmatched(number, 4) or
                prefixmatched(number, 5) or
                prefixmatched(number, 37) or 
                prefixmatched(number, 6)) and 
              ((sumofevenplace(number) + 
                sumofoddplace(number))%10 == 0))

if __name__=="__main__":
    number=int(input("Enter card number"))
    if(isvalid(number)):  
        print("Valid")
    else:
        print("invalid")
