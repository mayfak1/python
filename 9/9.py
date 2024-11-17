import random
vivod=[
    ['.','.','.','.'],
    ['.','.','.','.'],
    ['.','.','.','.'],
    ['.','.','.','.'],
]
k1=[]
k2=[]
k3=[]
k4=[]
b=[]
while (k1==k2 or k1==k3 or k1==k4 or k1==b or k2==k3 or k2==k4 or k2==b or k3==k4 or k3==b or k4==b):
    k1=[random.randint(0,3),random.randint(0,3)]
    k2=[random.randint(0,3),random.randint(0,3)]
    k3=[random.randint(0,3),random.randint(0,3)]
    k4=[random.randint(0,3),random.randint(0,3)]
    b=[random.randint(0,3),random.randint(0,3)]
k=1
k1f=0
k2f=0
k3f=0
k4f=bf=0
print(*b)
while 1:
    for i in vivod:
        print(*i)
    if k1f==k2f==k3f==k4f==1:
        print("Победа! Вы выиграли за", k , "попыток")
        break
    if bf==1:
        print("Бомба, вы проиграли на",k,"попытке")
        break

    print("Сделайте выстрел! Это ваша",k,"попытка")
    vistrel=[int(i)-1 for i in input().split()]
    k += 1
    if vistrel==k1:
        print("Попал!")
        vivod[k1[0]][k1[1]]="X"
        k1f=1
    elif vistrel==k2:
        print("Попал!")
        vivod[k2[0]][k2[1]]="X"
        k2f=1
    elif vistrel==k3:
        print("Попал!")
        vivod[k3[0]][k3[1]]="X"
        k3f=1
    elif vistrel==k4:
        print("Попал!")
        vivod[k4[0]][k4[1]]="X"
        k4f=1
    elif vistrel==b:
        vivod[b[0]][b[1]]="B"
        bf=1
    else:
        print("Мимо")

