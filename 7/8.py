a=input()
b=a.split()
a=a.replace(b[-1],'')
b=b[-1].split(':')
if int(b[0])>int(b[1]):
    print(a.split('-')[0])

elif int(b[0])<int(b[1]):
    print(a.split('-')[1])
else:
    print("Ничья")
