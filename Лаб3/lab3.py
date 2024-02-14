class Student:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class PhoneDirectory:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        student = Student(name, phone)
        self.contacts.append(student)
        print(f"Контакт {name} з номером {phone} додано до телефонного довідника.")

    def remove_contact(self, name):
        for student in self.contacts:
            if student.name == name:
                self.contacts.remove(student)
                print(f"Контакт {name} видалено з телефонного довідника.")
                return
        print(f"Контакт з ім'ям {name} не знайдено у телефонному довіднику.")

    def update_contact(self, name, new_phone):
        for student in self.contacts:
            if student.name == name:
                student.phone = new_phone
                print(f"Номер телефону для контакту {name} оновлено до {new_phone}.")
                return
        print(f"Контакт з ім'ям {name} не знайдено у телефонному довіднику.")

    def display_contacts(self):
        if self.contacts:
            print("Контакти у телефонному довіднику:")
            for student in self.contacts:
                print(f"Ім'я: {student.name}, Номер телефону: {student.phone}")
        else:
            print("Телефонний довідник порожній.")


def main():
    directory = PhoneDirectory()

    while True:
        print("\nМеню:")
        print("1. Додати контакт")
        print("2. Видалити контакт")
        print("3. Оновити контакт")
        print("4. Показати всі контакти")
        print("5. Вийти з програми")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            name = input("Введіть ім'я студента: ")
            phone = input("Введіть номер телефону: ")
            directory.add_contact(name, phone)
        elif choice == '2':
            name = input("Введіть ім'я студента, якого потрібно видалити: ")
            directory.remove_contact(name)
        elif choice == '3':
            name = input("Введіть ім'я студента, якому потрібно оновити номер телефону: ")
            new_phone = input("Введіть новий номер телефону: ")
            directory.update_contact(name, new_phone)
        elif choice == '4':
            directory.display_contacts()
        elif choice == '5':
            print("Дякую за використання програми. До побачення!")
            break
        else:
            print("Некоректний вибір. Будь ласка, виберіть опцію з меню.")

if __name__ == "__main__":
    main()
