n=int(input())
l=list(map(int,input().split()))
t=1
p=[]
for i in range(n-1):
	for j in range(i+1,n):
		c=l[i:j+1]
		for k in c:
			t=t*k
		p.append(t)
		t=1
p.sort()
print(p[-1])