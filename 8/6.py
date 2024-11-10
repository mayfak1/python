import random
k_r=0
k_o=0
k=0
while k_r!=3 and k_o!=3:
    m=random.randint(0,1)
    if m==0:
        print('Р', end=' ')
        k_r+=1
        k_o=0
    elif m==1:
        print('O',end=' ')
        k_o+=1
        k_r=0
    k+=1
print('(попыток ',k,')',sep='')