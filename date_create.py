import datetime
import csv

def have_note(name):
    with open('notebook.csv', 'r', encoding = 'utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[1].strip() == name:
                return True
        return False
    

def input_name():
    return input('Введите заголовок заметки: ')

def input_body():
    return input('Введите текст заметки: ')

def create_note():
    name = input_name()
    while have_note(name):
        print('Такая заметка уже есть! Введите другое название: ')
        name = input()
    body = input_body()
    date = datetime.date.today().isoformat()

    return f'{date}, {name}, {body};\n'

def create_changing_note(old_note, new_body):
    note = old_note.split(',')
    name = note[1].strip()
    body = new_body
    date = datetime.date.today().isoformat()

    return f'{date}, {name}, {body}'
