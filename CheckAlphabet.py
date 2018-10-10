n=input()
if(len(n)==1 and n.isalpha()):
    if((n>='A' and n<='Z') or (n>='a' and n<='z')):
        print("Alphabet")
    else:
        print("No")
else:
    print("No")
