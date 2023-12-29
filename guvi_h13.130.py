def prime(n):
    c=n//2
    f=1
    for i in range(2,c+1):
        if(n%i==0):
            f=0
            break
    if(f==1):
        return 1
    else:
        return 0
def main():
    n=int(input())
    c=0
    for j in range(2,n+1):
        if(j%10==3):
            r=prime(j)
            if(r==1):
                c+=j
    print(c)

main()