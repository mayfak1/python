d={1:'.,?!:',2:'ABC',3:'DEF',4:'GHI',5:'JKL',6:'MNO',7:'PQRS',8:'TUV',9:'WXYZ',0:' '}

s = input().upper()
k=0
res=''
while(k!=len(s)):
    for i in range(len(d)):
        for j in range(len(d[i])):
            if k==len(s):break
            if d[i][j]==s[k]:
                res+=str(i)*(j+1)
                k+=1
print(res)