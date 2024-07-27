rows=int(input("Enter no.of rows : "))
col=int(input("Enter no.of columns : "))
arr=[[0 for i in range(rows)] for i in range(col)]
for i in range(rows):
    for j in range(col):
        arr[i][j]=i*j
print(arr)