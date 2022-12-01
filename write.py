# Ф-ция ввода нового контакта в телефонную книгу.
# Формат ввода: Фамилия, Имя, Телефон, Описание.

import re
import csv
from create_phonebook_csv import phonebook_csv
from create_phonebook_csv import phonebook_header

def write():
    
    new_contact = []
    for element in phonebook_header:
        new_contact.append(input(f'Заполните поле: {element} \n'))

    with open(phonebook_csv, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(new_contact)
        print("Контакт успешно сохранен!")
    return True


