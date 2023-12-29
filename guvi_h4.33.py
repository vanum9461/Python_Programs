s=input()
i,m=0,0
strp=""
while i<len(s)-1:
  if s[i]=='a' and s[i+1]=='b':
    strp=strp+s[i]+s[i+1]
    i=i+2
  else:
    strp=""
    i+=1
  if m<len(strp):
    m=len(strp)
l=len(s)-1
if s[l]=="a" and s[l-1]=="b" and strp!="":
  m=m+1
print(m)