
number = int(input("Введите трехзначное число: "))


if 100 <= number <= 999:

    hundreds = number // 100         
    tens = (number // 10) % 10       
    units = number % 10              


else:
    print("Ошибка: Введите трехзначное число.")
