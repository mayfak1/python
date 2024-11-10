import random
zag='QWERTYUIOPASDFGHJKLZXCVBNM'
stroch=zag.lower()
cifr='1234567890'
spec='!@#$%^&*()"№%:,.;'
m=[]
k=int(input('Введите длину пароля'))
if input('нужны ли заглавные буквы (да/нет)')=='да':
    m+=zag
if input('нужны ли строчные буквы (да/нет)')=='да':
    m+=stroch
if input('нужны ли цифры (да/нет)')=='да':
    m+=cifr
if input('нужны ли специальные символы (да/нет)')=='да':
    m+=spec
print(''.join(random.choices(m,k=k)))
