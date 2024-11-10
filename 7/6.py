a=input()
if a[-1]=='#':
    otv=''
    ind=[]
    a=a[:-1]
    k=len(a)
    for i in range(1,len(a)+1,2):
        ind.append(i-1)
    if len(a)%2==0:
        for i in range(len(a),1,-2):
            ind.append(i-1)
    else:
        for i in range(len(a)-1,1,-2):
            ind.append(i-1)
    for i in ind:
        otv+=a[i]
    print(otv)


else:
    print('нет символа')