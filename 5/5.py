
a = float(input("Введите длину первой стороны треугольника: "))
b = float(input("Введите длину второй стороны треугольника: "))
c = float(input("Введите длину третьей стороны треугольника: "))


if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        triangle_type = "равносторонний"
    elif a == b or b == c or a == c:
        triangle_type = "равнобедренный"
    else:
        triangle_type = "разносторонний"
    

    print(f"Треугольник является {triangle_type}.")
else:
    print("Ошибка: Длины сторон не могут образовать треугольник.")
