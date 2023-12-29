def checksubstring(s,p):
    m,n=len(s),len(p)
    for i in range(m-n+1):
        for j in range(n):
            if(s[i+j]!=p[j]):
                break
        if(j+1==n):
            return 1
    return -1
if __name__ == "__main__":
    s,p=map(str,input().split())
    res=checksubstring(s,p)
    if(res==-1):
        print("no")
    else:
        print("yes")
