def printIntersection(arr1, arr2, m, n):
    i,j = 0,0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j+= 1
        else:
            return(arr2[j])
            j += 1
            i += 1

if __name__=="__main__":
    
    t = int(input())
    while t>0:
        n=int(input())
        arr1.list(map(int, input().split()))
        arr2.list(map(int, input().split()))
        m = len(arr1)
        n = len(arr2)
        p=printIntersection(arr1, arr2, m, n)
        t=arr1.index(p)
        print(round(abs((n/2)-(t+1))))    
