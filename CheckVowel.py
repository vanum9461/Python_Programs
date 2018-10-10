n=input()
l=['a','e','i','o','u','A','E','I','O','U']
if(len(n)==1 and n.isalpha()):
    if(n in l):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
