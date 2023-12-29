import random
deck=[x for x in range(0,52)]
#print(*deck)
random.shuffle(deck)
ranks=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits=["Hearts","Spades","Clubs","Diamonds"]
p1=deck[0:26]
p2=deck[26:52]
print(*p1)
print(*p2)
for i in range(26):
    if(rank[p1[i]]==rank[p2[i]]):
        print("p2 wins")
        break
    
        

"""for card in deck:
       rank=ranks[card%13]
       suit=suits[card//13]
       print(rank +" of " + suit)
"""
