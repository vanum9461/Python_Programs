n=int(input())
l=list(map(int,input().strip().split()))
l.sort(reverse=True)
print(*l,sep="")