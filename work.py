import os

FILENAME = "phonebook.txt"

def load_contacts():

    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        contacts = [line.strip().split(",") for line in file]
    return [{"name": contact[0], "phone": contact[1]} for contact in contacts]

def save_contacts(contacts):

    with open(FILENAME, "w", encoding="utf-8") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")

def add_contact(contacts):
    """Добавить новый контакт."""
    name = input("Введите имя: ").strip()
    phone = input("Введите номер телефона: ").strip()
    contacts.append({"name": name, "phone": phone})
    print("Контакт добавлен.")

def search_contact(contacts):

    search = input("Введите имя или номер для поиска: ").strip().lower()
    found = [c for c in contacts if search in c["name"].lower() or search in c["phone"]]
    if found:
        for contact in found:
            print(f"Имя: {contact['name']}, Телефон: {contact['phone']}")
    else:
        print("Контакты не найдены.")

def edit_contact(contacts):

    name = input("Введите имя контакта для изменения: ").strip()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            new_name = input("Введите новое имя (оставьте пустым, чтобы не изменять): ").strip()
            new_phone = input("Введите новый номер телефона (оставьте пустым, чтобы не изменять): ").strip()
            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            print("Контакт обновлен.")
            return
    print("Контакт не найден.")

def delete_contact(contacts):

    name = input("Введите имя контакта для удаления: ").strip()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Контакт удален.")
            return
    print("Контакт не найден.")

def main():

    contacts = load_contacts()
    while True:
        print("\nТелефонная книжка")
        print("1. Добавить контакт")
        print("2. Найти контакт")
        print("3. Изменить контакт")
        print("4. Удалить контакт")
        print("5. Показать все контакты")
        print("6. Выйти")
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            for contact in contacts:
                print(f"Имя: {contact['name']}, Телефон: {contact['phone']}")
        elif choice == "6":
            save_contacts(contacts)
            print("Изменения сохранены. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
