n,m =[int(i) for i in input().split()]
zal=[]
f=True
for _ in range(n):
    ryad=[int(i) for i in input().split()]
    if len(ryad)!=m:
        f=False
        print("ошибка")
        break
    zal.append(ryad)
if f:
    ff=1
    k=int(input())
    kk=0
    for i in range(len(zal)):
        if ff:
            for j in zal[i]:
                if j==0:
                    kk+=1
                    if k==kk:
                        print(i+1)
                        ff=0
                        break

                else: kk=0
    if ff:
        print(0)

