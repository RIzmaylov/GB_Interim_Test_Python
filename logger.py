import csv

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

def search_note():
    search = str(input('Введите название искомой заметки: '))

    with open('notebook.csv', 'r', encoding = 'utf-8') as file:
        reader = csv.reader(file, delimiter=',')

        for row in reader:
            if row[1].strip() == search:
                print(' '.join(row))

def change_note():
    search = str(input('Введите название заметки для изменения: '))

    with open('notebook.csv', 'r+', encoding = 'utf-8') as file:
        notes = file.read().split(';')

        index = -1
        for row in notes:
            note = row.split(',')
            print(' '.join(note))
            if note[1].strip() == search:
                index = notes.index(row)
        if index == -1:
            print('Нет заметки с таким названием')
            return
        print('Старая заметка: ')
        print(notes[index])
        note_body = input('Введите новое тело заметки: ')
        note = notes[index].split(',')
        note[2] = note_body
        notes[index] = note
