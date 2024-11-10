a=input().split()
b=[]
c=[]
for i in a:
    if i.isdigit():
        b.append(i)
    else:
        c.append(i)
print(*b)
print(*c)