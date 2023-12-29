def toString(list):
    return "".join(list)
def permute(s,l,r):
    if(l==r):
        print(toString(s))
    else:
        for i in range(l,r+1):
            s[l],s[i]=s[i],s[l]
            permute(s,l+1,r)
            s[l],s[i]=s[i],s[l]

if __name__ == "__main__":
    s=input()
    n=len(s)
    l=list(s)
    permute(l,0,n-1)