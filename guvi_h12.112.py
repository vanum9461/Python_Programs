def lcs(n,m,x,y):
    L=[[0 for i in range(y+1)] for i in range(x+1)]
    for i in range(x+1):
        for j in range(y+1):
            if(i==0 or j==0):
                L[i][j]=0
            elif(n[i-1]==m[j-1]):
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    a1=L[x][y]
    lcs=[""]*(a1+1)
    lcs[a1]=""
    i,j=x,y
    while(i>0 and j>0):
        if(n[i-1]==m[j-1]):
            lcs[a1-1]=n[i-1]
            i-=1
            j-=1
            a1-=1
        elif(L[i-1][j]>L[i][j-1]):
            i-=1
        else:j-=1
    print("".join(lcs))

if __name__ == "__main__":
    n=str(input())
    m=str(input())
    lcs(n,m,len(n),len(m))
