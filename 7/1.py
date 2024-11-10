a=input().split()
b=[]
for i in range(len(a)):
    if a[i]!=a[i-1]:
        b.append(a[i])
print(' '.join(b))
