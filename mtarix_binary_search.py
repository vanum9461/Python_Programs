row = int(input("Enter no of rows  "))
col = int(input("Enter no of columns  "))
mat = [[0]*col]*row     #Intialising a 2d matrix with 0
print("Enter elements of matrix separated by space/hit enter for new row: ")
for i in range(row):
    mat[i] = list(map(int,input().strip().split(" ")))
key = int(input("Enter the element to be searched: "))
i , j = 0 , len(mat[0])-1
while mat[i][j] != key:
    if key < mat[i][j] and j>0:
        j-=1
    elif key > mat[i][j] and i<(row-1):
        i+=1
    else:
        break
if mat[i][j] == key:
    print("Element found at position ({0},{1})".format(i,j))
else:
    print("Element not found in matrix")
