n,m=map(int,input().split())
a=[]
for i in range(0,n):
  a.append(list(map(int,input().split())))
for i in range(0,n):
  for j in range(0,m):
    if a[i][j]==0:
      for k in range(0,m):
        a[i][k]=8
      for k1 in range(0,n): 
        a[k1][j]=8
for i in range(0,n):
  for j in range(0,m):
    if a[i][j]==8:
      a[i][j]=0
for i in a:
  print(*i)
    