a=input()
glas='уеыаоэёяию'
if a.count("/")==2:
    a=a.split('/')
    k1=0
    k2=0
    k3=0
    for g in glas:
        k1+=a[0].lower().count(g)
    for g in glas:
        k2+=a[1].lower().count(g)
    for g in glas:
        k3+=a[2].lower().count(g)
    if k1==5 and k2==7 and k3==5:
        print("Хайку")
    else:
        print("Не хайку")

    

else:
    print("Не хайку. Должно быть 3 строки")

#Вечер за окном. / Еще один день прожит. / Жизнь скоротечна...
#Просто текст
#Как вишня расцвела! / Она с коня согнала / И князя-гордеца.