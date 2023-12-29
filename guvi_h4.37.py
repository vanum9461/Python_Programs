s=input()
a=""
for i in range(len(s)):
    a=s[:i]+s[i+1:]
    if a==a[::-1]:
        c=0
        break
    else:
        c=1
   
if c==0:
    print("YES")
else:
    print("NO")