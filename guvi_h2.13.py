if __name__ == "__main__":
    s=input()
    stack=[]
    flag=True
    n=len(s)
    if(n%2!=0):
        for i in range((n//2)+1):
            stack.append(s[i])
    else:
        for i in range((n//2)):
            stack.append(s[i])
        
    for i in range((n//2),n):
        if(s[i]!=stack.pop()):
            print('NO')
            flag=False
            break
    if(flag):
        print('YES')
        