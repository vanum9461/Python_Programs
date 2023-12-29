n,k=map(int,input().split())
l=list(map(int,input().split()))
p=[]
for i in l:
	if i!=k:
		p.append([i,abs(k-i)])
p.sort(key=lambda x:x[1])
print(str(p[0][0])+" "+str(p[1][0])+" "+str(p[2][0]))