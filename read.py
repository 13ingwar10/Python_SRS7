# Функция поиска контактов
import pandas as pd
from create_phonebook_csv import phonebook_csv

def read():
    print('Нажатие Enter без ввода значения выведет все контакты')
    print('Введите "Фамилию": ')
    key_word = []
    key_word = list(map(str, input().split()))

    df = pd.read_csv(phonebook_csv, sep=',', header=None)
    df = df[1:]     # Удаляем заголовок
    df.columns = ['Фамилия', 'Имя', 'Номер телефона', 'Описание']

    if len(key_word) == 0:
        print(df)
        return True
    else:
        df_new = df.loc[df['Фамилия'] == key_word[0]]
        if df_new.shape[0]:
            print(df_new)
        else:
            print('Контакта с такой Фамилией нет.')
        return True