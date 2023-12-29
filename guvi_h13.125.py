def mostfrequent(list):
    p=set(list)
    d=dict()
    for i in range(len(list)):
        if(list[i] in d.keys()):
            d[list[i]]+=1
        else:
            d[list[i]]=1
    for i in d:
        if(d[i]>1):
            p.remove(i)
    print("".join(p))

def main():
    n=input()
    l=list(n)
    mostfrequent(l)

main()