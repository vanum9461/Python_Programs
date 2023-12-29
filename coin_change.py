def coinchange(amt,coin):
	n=[0]*(amt+1)
	n[0]=1
	for i in range(len(coin)):
		for j in range(amt+1):
			if(j>=coin[i]):
				n[j]+=n[j-coin[i]]
		print(*n)
	return n[amt]

print(coinchange(12,[1,2,5]))