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
    command = input('Выберите действие: \n1 - добавить новый контакт \n2 - поиск контакта \n3 - завершить работу \n')
    if command.lower() == '1':
        command = write()
        txt = 'ОК!' if command else 'ERROR!'
        log('Создание нового контакта', txt)
        print('-' * 10)
    elif command.lower() == '2':
        command = read()
        txt = 'ОК!' if command else 'ERROR!'
        log('Поиск контактов', txt)
        print('-' * 10)
    elif command.lower() == '3':
        break
    else:
        print('Ошибка! Такой команды нет')

