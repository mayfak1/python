import math
count = int(input())
lst=[[0 for j in range(2)] for i in range(count)]


for i in range(count):
    a=input()
    
    lst[i][0]=int(a.split()[0])
    lst[i][1]=int(a.split()[1]) 
user=list(map(int ,input().split()))
min=10000
res=0
for i in range(count):
    a=math.sqrt((((lst[i][0]-user[0])**2)+((lst[i][1]-user[1])**2)))
    if a <min:
        min=a
        res=i
print(lst[res])
