def choose():
    return input(
        'Укажите, какое действие произвести:'
        '1 - добавить контакт, 2 - найти контакт):\n')


def new():
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    return (f'{name} : {phone}')


def what_to_search():
    return input('Что будем искать? \n')


def show_result(result):
    print('Вот то, что удалось найти: ')
    for i in result:
        print(i)
