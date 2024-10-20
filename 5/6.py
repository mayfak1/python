
days_in_month = {
    "январь": 31,
    "февраль": "28 или 29 (в зависимости от високосного года)",
    "март": 31,
    "апрель": 30,
    "май": 31,
    "июнь": 30,
    "июль": 31,
    "август": 31,
    "сентябрь": 30,
    "октябрь": 31,
    "ноябрь": 30,
    "декабрь": 31
}


month = input("Введите название месяца: ")


if month in days_in_month:
    print(f"Количество дней в {month}: {days_in_month[month]}")