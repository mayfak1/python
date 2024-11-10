x=int(input())
a=list(map(int,input().split()))
k=1
for i in a:
    if x>i:
        print(k)
        break
    k+=1
else:
    print(k)
