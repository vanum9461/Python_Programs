p,q=map(str,input().split())
p,q=list(p),list(q)
digit=1 
while(abs(len(p)-len(q))!=0):
    if(len(p)>len(q)):
        q.append(digit)
        digit+=1 
    else:
        p.append(digit)
        digit+=1 
for i in range(len(p)):
    print(p[i],end="")
    print(q[i],end="")