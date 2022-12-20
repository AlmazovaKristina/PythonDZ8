def main_menu():
    print('\n1. Показать телефонную книгу')
    print('2. Открыть файл телефонной книги')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт ')
    print('0. Выход\n')
    return choice_main_menu()


def choice_main_menu():
    while True:
        try:
            choice = int(input('Введите команду из меню: '))
            if choice in range(0, 8):
                print()
                return choice
            else:
                print('Такого пункта нет, повторите попытку ')
        except:
            print('Ошибка ввода! Некорректные данные!')


def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book):
            print(id, *contact)
    else:
        print('Телефонная книга пуста или не загружена')


def log_off():
    print('До свидания, до новых встреч!')


def load_success():
    print('Телефонная книга загружена')


def save_success():
    print('Телефонная книга сохранена')

def remove_success():
    print('Контакт удалён')


def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Ведите телефон контакта: ')
    comment = input('Введите коментарий к контакту ')
    return [name, phone, comment]

def input_remove_contact():
    id = int(input('Введите ID контакт, которий хотите удалить: '))
    return id


def input_change_contact():
    id = int(input('Введите ID контакт, которий хотите изменить: '))
    return id

def input_new_change_contact():
    newname = input('Введите новое имя контакта: ')
    newphone = input('Ведите новый телефон контакта: ')
    newcomment = input('Введите новый коментарий к контакту ')
    return [newname, newphone, newcomment]

def input_massage(contact):
    print(f'Контакт "{contact[0]}" успешно изменён')


def str_serch_contact():
    serch = input('Введите кого необходимо найти: ')
    return serch

def print_serch(result2):
    print(f'Вот что удалось найти: {result2}')