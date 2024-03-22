import datetime

def input_name():
    return input('Введите заголовок заметки: ')

def input_body():
    return input('Введите текст заметки: ')

def create_note():
    name = input_name()
    body = input_body()
    date = datetime.date.today().isoformat()

    return f'{date}, {name}, {body};\n'
