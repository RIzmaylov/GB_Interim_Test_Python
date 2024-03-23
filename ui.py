from date_create import *
from logger import *

def interface():
    with open('notebook.csv', 'a'):
        pass

    command = -1
    while command != '6':
        print('Выберите вариант взаимодействия:\n'
            '1. Добавить заметку\n'
            '2. Редактировать заметку\n'
            '3. Поиск нужной заметки по названию\n'
            '4. Удалить заметку\n'
            '5. Вывод заметок за промежуток времени\n'
            '6. Выход из программы')
        print()
        command = input('Введите номер команды: ')

        while command not in ('1', '2', '3', '4', '5', '6'):
            print('Введите корректный номер меню!')
            command = input('Введите номер команды: ')

        match command:
            case '1':
                add_note(create_note())
            case '2':
                change_note()
            case '3':
                search_note()
            case '4':
                del_note()
            case '5':
                show_notebook()
            case '6':
                print('Всего хорошего!')
