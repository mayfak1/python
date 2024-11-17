n,m=[int(i) for i in input().split()]
matrix=[]
f=1
for _ in range(n):
    stroka=[]
    for _ in range(m):
        if f:
            stroka.append(1)
        else:
            stroka.append(0)
    f=0
    matrix.append(stroka)
for i in range(len(matrix)):
    matrix[i][0]=1
for i in range(1,len(matrix)):
    for j in range(1,len(matrix[i])):
        matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
for i in matrix:
    print(*i)