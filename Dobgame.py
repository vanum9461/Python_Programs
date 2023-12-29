if __name__ == "__main__":
    a=[[],[],[],[],[]]
    for i in range(1,32):
        n=bin(i)
        if(len(n)==3):
           if(n[2]=='1'):
               a[0].append(i)
        if(len(n)==4):
           if(n[3]=='1'):
               a[0].append(i)
           if(n[2]=='1'):
               a[1].append(i)
        if(len(n)==5):
           if(n[4]=='1'):
               a[0].append(i)
           if(n[3]=='1'):
               a[1].append(i)
           if(n[2]=='1'):
               a[2].append(i)
        if(len(n)==6):
           if(n[5]=='1'):
               a[0].append(i)
           if(n[4]=='1'):
               a[1].append(i)
           if(n[3]=='1'):
               a[2].append(i)
           if(n[2]=='1'):
               a[3].append(i)
        if(len(n)==7):
           if(n[6]=='1'):
               a[0].append(i)
           if(n[5]=='1'):
               a[1].append(i)
           if(n[4]=='1'):
               a[2].append(i)
           if(n[3]=='1'):
               a[3].append(i)
           if(n[2]=='1'):
               a[4].append(i)
    sum=0
    for i in range(5):
        print(a[i])
        print()
        print("*******************************************************")
        print()
        print("Enter 'yes' if list contain your birth date else enter 'no'")
        print()
        ch=input()
        print()
        if(ch=="yes"):
            sum+=2**i
    print("Your date of birth is :",sum)
