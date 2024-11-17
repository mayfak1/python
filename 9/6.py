a=int(input())
matrix=[[0 for b in range(a)]for j in range(a)]
for i in range(len(matrix)):
    s = list(map(int,input().split()))
    for j in range(len(matrix[i])):
        matrix[i][j]=s[j]
k=0
for i in range(2):
    prom=matrix[0][k]
    matrix[0][k]=matrix[a-1][k]
    matrix[a-1][k]=prom
    k=a-1
print(matrix)