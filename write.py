# Ф-ция ввода нового контакта в телефонную книгу.
# Формат ввода: Фамилия, Имя, Телефон, Описание.

import re
import csv
from create_phonebook_csv import phonebook_csv

def write():
    print('Введите через пробел: Фамилию, Имя, Телефон, Описание:')
    new_contact = list(map(str, input().split()))

    if len(new_contact) != 4:
        print('Ошибка: нужно заполнить 4 поля контакта: Фамилию, Имя, Телефон, Описание.')
        return False
    else:
        with open(phonebook_csv, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Создем заголовок таблицы для Phonebook.csv
            writer.writerow(new_contact)
        return True


