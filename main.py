# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах
# Под форматом понимаем структуру файлов
# В консоли предложить пользователю в каком режиме работает:
# 1) запись данных (ввести данные для записи (Фамилия, Имя, Телефон, Описание))
# 2) экспорт данных (получить данные из CSV файла, по Фамилии вывести все данные)

from log import log
from create_phonebook_csv import create_phonebook_csv
from write import write
from read import read

create_phonebook_csv()

while(True):
    command = input('Командная строка: ')
    if command.lower() == 'добавить':
        command = write()
        txt = 'ОК!' if command else 'ERROR!'
        log('Создание нового контакта', txt)
        print('-' * 10)
    elif command.lower() == 'найти':
        command = read()
        txt = 'ОК!' if command else 'ERROR!'
        log('Поиск контактов', txt)
        print('-' * 10)
    elif command.lower() == 'завершить':
        break
    else:
        print('Такой команды нет')

