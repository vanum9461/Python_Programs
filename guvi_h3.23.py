amu,m=map(int,input().split())
a=[]
for x in range(amu):
  a.append(list(map(int,input().split())))
post,arr,temp,t=[],[],[],[]
i,j=0,0
arr.append(a[i][j])
post.append([i,j])
while [amu-1,m-1] not in post:
  i=0
  for x in post:
    if x[0]+1<amu and x[1]+1<m:
      temp.append(a[x[0]+1][x[1]]+arr[i])
      temp.append(a[x[0]][x[1]+1]+arr[i])
      t.append([x[0]+1,x[1]])
      t.append([x[0],x[1]+1])
    elif x[0]+1<amu:
      temp.append(a[x[0]+1][x[1]]+arr[i])
      t.append([x[0]+1,x[1]])
    elif x[1]+1<m:
      temp.append(a[x[0]][x[1]+1]+arr[i])
      t.append([x[0],x[1]+1])
    i+=1
  post=t
  t=[]
  arr=temp
  temp=[]
print(max(arr))