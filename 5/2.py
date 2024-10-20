
N = int(input("Введите число N: "))
K = int(input("Введите количество последних цифр K для отрезания: "))



result = N // (10 ** K)


print("Число без последних K цифр:", result)


last_digits = N % (10 ** K)
print("Последние K цифр:", last_digits)
