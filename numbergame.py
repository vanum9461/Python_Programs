import random
x=random.randint(0,9)
y=random.randint(0,9)
print("what is {} +/- {}".format(x,y))
if(x>y):
    a=int(input())
    if(a==1):
        b=int(input())
        if(b==(x+y)):
            print("Correct")
        else:
            print("Wrong")
            
    else:
        b=int(input())
        if(b==(x-y)):
            print("Correct")
        else:
            print("Wrong")
else:
    print("try again")
