#call by reference in immutable objects
#effects can be seen in mutable-list,tuple

def increment(n):
    print("The value of n is",id(n))
    n+=1
    print("The value of n is",id(n))
    return n

def main():
    a=10
    #print("The value of a is",a)
    print("The value of a is",id(a))
    c=increment(a)
    print("The value of a is",id(a))
    print(id(c))

main()
