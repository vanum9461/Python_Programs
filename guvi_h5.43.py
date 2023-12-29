s=input()
x=""
if len(s)%2==0:
	for i in range(len(s)):
		if i%2==1:
			if int(s[i])%2==0:
				x+=s[i-1]*int(s[i])
			else:
				x+=s[i-1]+s[i]
else:
	for i in range(len(s)-1):
		if i%2==1:
			if s[i].isdigit() and s[i+1].isdigit():
				m=int(s[i])*10+int(s[i+1])
				if m%2==0:
					x+=s[i-1]*m
				else:
					x+=s[i-1]+str(m)
			elif int(s[i])%2==0:
				x+=s[i-1]*int(s[i])
			else:
				x+=s[i-1]+s[i]
print(x)