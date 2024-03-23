import csv
from date_create import create_changing_note

def add_note(note):
    with open('notebook.csv', 'a', encoding = 'utf-8') as file:
        file.write(note)
    print('Заметка успешно сохранена\n')

def date_request():
     print('Введите с какой даты вывести заметки')
     year_from = int(input('Введите год '))
     month_from = int(input('Введите номер месяца '))
     day_from = int(input('Введите число '))
     print('Введите по какую дату включительно вывести заметки')
     year_to = int(input('Введите год '))
     month_to = int(input('Введите номер месяца '))
     day_to = int(input('Введите число '))
     return [[year_from, month_from, day_from], [year_to, month_to, day_to]]

def l_date_yearlier_than_r(l_date, r_date):
    if l_date[0] < r_date[0]:
        return True
    if l_date[0] == r_date[0]:
        if l_date[1] < r_date[1]:
            return True
        if l_date[1] == r_date[1]:
            if l_date[2] <= r_date[2]:
                return True
    return False

def show_notebook():
    with open('notebook.csv', 'r', encoding = 'utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        req = input('Хотите вывести заметки за определенный промежуток времени? (Y/N) ')
        if (req == 'Y' or req == 'y'):
            dates = date_request()
            for row in reader:
                date = row[0].split('-')
                int_date = [int(item) for item in date]
                if l_date_yearlier_than_r(dates[0], int_date) and l_date_yearlier_than_r(int_date, dates[1]):
                    print(' '.join(row))
        else:
            for row in reader:
                date = row[0].split('-')
                print(' '.join(row))

def index_of_name(search):
    with open('notebook.csv', 'r', encoding = 'utf-8') as file:
        notes = file.read().split(';\n')

        index = -1
        for row in notes:
            note = row.split(',')
            if len(note) == 3 and note[1].strip() == search:
                index = notes.index(row)
        return index

def search_note():
    search = str(input('Введите название искомой заметки: '))

    with open('notebook.csv', 'r', encoding = 'utf-8') as file:
        notes = file.read().split(';\n')
        index = index_of_name(search)
        if index == -1:
            print('Нет заметки с таким названием\n')
            return
        print('Ваша заметка:')
        print(notes[index] + '\n')

def change_note():
    search = str(input('Введите название заметки для изменения: '))

    file = open('notebook.csv', 'r+', encoding = 'utf-8')
    notes = file.read().split(';\n')

    index = index_of_name(search)
    if index == -1:
        print('Нет заметки с таким названием\n')
        return
    print('Старая заметка: ')
    print(notes[index] + '\n')
    note_body = input('Введите новое тело заметки: ')
    notes[index] = create_changing_note(notes[index], note_body)
    print('Заметка изменена: ')
    print(notes[index] + '\n')

    file = open('notebook.csv', 'w', encoding = 'utf-8')
    file.writelines(f'{item};\n' for item in notes if len(item) > 1)

def clear_file():
    with open('notebook.csv', 'w', encoding = 'utf-8') as file:
        pass

def del_note():
    search = str(input('Введите название заметки для удаления: '))

    file = open('notebook.csv', 'r+', encoding = 'utf-8')
    notes = file.read().split(';\n')
    index = index_of_name(search)
    if index == -1:
        print('Нет заметки с таким названием\n')
        return
    print('Следующая заметка будет удалена: ')
    print(notes[index])
    req = input('Удалить? (Y/N): ')
    if (req == 'Y' or req == 'y'):
        file = open('notebook.csv', 'w', encoding = 'utf-8')
        file.writelines(f'{item};\n' for item in notes if len(item) > 1 and notes.index(item) != index)

    # with open('notebook.csv', 'r+', encoding = 'utf-8') as file:
    #     notes = file.read().split(';\n')

    #     index = index_of_name(search)
    #     if index == -1:
    #         print('Нет заметки с таким названием\n')
    #         return

    #     print('Следующая заметка будет удалена: ')
    #     print(notes[index])
    #     req = input('Удалить? (Y/N): ')
    #     if (req == 'Y' or req == 'y'):
    #         notes.pop(index)
    #         clear_file()
    #         file.writelines(f'{item};\n' for item in notes if len(item) > 1)