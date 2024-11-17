
restaurant_menu = [
    ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
    ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
    ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]

def display_menu():
    for dish in restaurant_menu:
        print(dish[0], 'Цена -', dish[2])

def find_dish():
    dish_name = input('Введите название блюда: ')
    for dish in restaurant_menu:
        if dish_name in dish:
            print('Ингредиенты -', *dish[1], '\nЦена -', dish[2])
            break
    else:
        print("Блюдо не найдено")

def add_dish():
    new_dish = []
    new_dish.append(input('Введите название блюда: '))
    ingredients = []
    print("Введите ингредиенты блюда (чтобы завершить ввод, напишите 0):")
    ingredient_input = input()
    while ingredient_input != '0':
        ingredients.append(ingredient_input)
        ingredient_input = input()
    new_dish.append(ingredients)
    new_dish.append(int(input("Введите цену блюда: ")))
    restaurant_menu.append(new_dish)

def change_price():
    dish_name = input('Введите название блюда: ')
    for index in range(len(restaurant_menu)):
        if dish_name in restaurant_menu[index]:
            restaurant_menu[index][2] = int(input("Введите новую цену блюда: "))
            break
    else:
        print("Блюдо не найдено")

while True:
    print("""1. Отобразить меню ресторана.
2. Найти блюдо по названию и отобразить его ингредиенты и цену.
3. Добавить новое блюдо в меню.
4. Изменить цену блюда.
5. Выйти""")
    user_choice = input()
    if user_choice == '1':
        display_menu()
    elif user_choice == '2':
        find_dish()
    elif user_choice == '3':
        add_dish()
    elif user_choice == '4':
        change_price()
    elif user_choice == '5':
        break
    else:
        print("Ввод не ясен")
