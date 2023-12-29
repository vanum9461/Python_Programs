def mostfrequent(list):
    d=dict()
    for i in range(len(list)):
        if(list[i] in d.keys()):
            d[list[i]]+=1
        else:
            d[list[i]]=1
    m,t=0,-1
    for i in d:
        if(m<d[i]):
            t=i
            m=d[i]
    print(t)

def main():
    n=int(input())
    l=list(map(int,input().strip().split()))
    mostfrequent(l)

main()