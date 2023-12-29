def main():
    t=int(input())
    while(t>0):
        c=1
        n=int(input())
        arr=list(map(int,input().strip().split())
        for i in range(n):
            for j in range(c):
                c+=arr[i]
            if c>=n:
                break
        print(i+1)
        t-=1
        
main()
