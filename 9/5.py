a = list(map(int,input().split()))
matrix=[[0 for j in range(int(a[1])) ]for g in range(int(a[0]))]
matrix_new=[[0 for j in range(int(a[0])) ]for g in range(int(a[1]))]
    
for i in range(len(matrix)):
    s = list(map(int,input().split()))
    for j in range(len(matrix[i])):
        matrix[i][j]=s[j]
        matrix_new[j][i]=matrix[i][j]

        
print(matrix_new)