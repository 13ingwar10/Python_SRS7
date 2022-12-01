# Функция создания новой телефонной книги если она отсутствует
from os.path import exists
import csv

phonebook_csv = 'Phonebook.csv'
phonebook_header = ['Фамилия', 'Имя', 'Номер телефона', 'Описание']

def create_phonebook_csv():
    global phonebook_header
    if not exists(phonebook_csv):
        with open(phonebook_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Создем заголовок таблицы для Phonebook.csv
            writer.writerow(phonebook_header)